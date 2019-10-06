from flask import jsonify
from flask_restful import Resource
from sqlalchemy import func

from project.server.models import Question


class FermiQuestions(Resource):

    @staticmethod
    def get():

        question = Question.query.order_by(func.random()).limit(1).first()

        return jsonify(question.as_dict())
