from flask import jsonify
from flask_restful import Resource

from project.server.datasources.cities import Cities
from project.server.models import Question

from sqlalchemy.sql.expression import func

class FermiQuestions(Resource):
    @staticmethod
    def get():
        question = Question.query.order_by(func.random()).limit(1).first()

        q = Cities.get_questions()

        return jsonify(q.as_dict())
        return jsonify(question.as_dict())
