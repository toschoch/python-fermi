from flask import jsonify
from flask_restful import Resource
from sqlalchemy import func

from project.server.datasources import AllSources


class RandomFermiQuestions(Resource):

    @staticmethod
    def get():

        q = AllSources.get_question()

        return jsonify(q.as_dict())
