# project/server/main/views.py


from flask import render_template, Blueprint
from project.server import db
from project.server.models import Question

from sqlalchemy.sql.expression import func


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def home():
    question = Question.query.order_by(func.random()).limit(1).first().text
    #question = "test?" # "How many ants live on this planet earth?"
    return render_template("main/home.html", question=question)


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")
