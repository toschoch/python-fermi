# manage.py


import subprocess
import sys
import unittest

import click
import coverage
from flask.cli import FlaskGroup

from project.server import create_app, db
from project.server.static_questions import questions
from project.server.models import User, Question

app = create_app()
cli = FlaskGroup(create_app=create_app)

# code coverage
COV = coverage.coverage(
    branch=True,
    include="project/*",
    omit=[
        "project/tests/*",
        "project/server/config.py",
        "project/server/*/__init__.py",
    ],
)
COV.start()

@cli.command()
def create_admin():
    """Creates the admin user."""
    db.session.add(User(email="ad@min.com", password="admin", admin=True))
    db.session.commit()


@cli.command()
def create_data():
    """Creates sample data."""
    q = questions[0]
    query = db.session.query(Question).filter(Question.text == q.text)
    if not db.session.query(query.exists()).scalar():
        click.echo("The static questions don't seem to exist... add them")
        for q in questions:
            db.session.add(q)
        db.session.commit()
        click.echo("done")
    else:
        click.echo("questions already in database!")



@cli.command()
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover("project/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover("project/tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage Summary:")
        COV.report()
        COV.html_report()
        COV.erase()
        sys.exit(0)
    else:
        sys.exit(1)


@cli.command()
def flake():
    """Runs flake8 on the project."""
    subprocess.run(["flake8", "project"])


if __name__ == "__main__":
    cli()
