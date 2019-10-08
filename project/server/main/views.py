# project/server/main/views.py


from flask import render_template, Blueprint

from project.server.datasources import AllSources

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def home():
    q = AllSources.get_question()
    #question = "test?" # "How many ants live on this planet earth?"
    return render_template("main/home.html", question=q.text, units=q.unit.description)


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")
