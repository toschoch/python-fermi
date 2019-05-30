# project/server/user/views.py


from flask import render_template, Blueprint, url_for, redirect, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from project.server import bcrypt, db
from project.server.models import User, Question
from project.server.user.forms import LoginForm, RegisterForm, QuestionForm


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)

        flash("Thank you for registering.", "success")
        return redirect(url_for("user.questions"))

    return render_template("user/register.html", form=form)


@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
            user.password, request.form["password"]
        ):
            login_user(user)
            flash("You are logged in. Welcome!", "success")
            return redirect(url_for("user.questions"))
        else:
            flash("Invalid email and/or password.", "danger")
            return render_template("user/login.html", form=form)
    return render_template("user/login.html", title="Please Login", form=form)


@user_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out. Bye!", "success")
    return redirect(url_for("main.home"))


@user_blueprint.route("/questions", methods=["GET", "POST"])
@login_required
def questions():
    form = QuestionForm(request.form)
    if form.validate_on_submit():

        question = Question(form.text.data, form.answer.data,
                            uncertainty=form.uncertainty.data,
                            creator_id=current_user.get_id(),
                            source=form.source.data)
        db.session.add(question)
        db.session.commit()

        flash("Question added to database!", "success")
        return redirect(url_for("user.questions"))

    return render_template("user/questions.html", form=form)
