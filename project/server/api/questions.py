from flask import jsonify
from flask_restful import Resource

from project.server.datasources import AllSources

class FermiQuestions(Resource):

    @staticmethod
    def get():

        q = AllSources.get_question()

        return jsonify(q.as_dict())
