# project/server/user/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email Address", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired()])


class RegisterForm(FlaskForm):
    email = StringField(
        "Email Address",
        validators=[
            DataRequired(),
            Email(message=None),
            Length(min=6, max=40),
        ],
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        "Confirm password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )


class QuestionForm(FlaskForm):
    text = StringField(
        "Question",
        validators=[
            DataRequired()
        ]
    )
    answer = FloatField(
        "Answer",
        validators=[
            DataRequired()
        ]
    )
    uncertainty = FloatField(
        "Uncertainty"
    )
