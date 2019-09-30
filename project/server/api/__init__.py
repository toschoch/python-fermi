from flask import Blueprint
from flask_restful import Api
from .questions import FermiQuestions

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

# add resources
api.add_resource(FermiQuestions, '/questions')