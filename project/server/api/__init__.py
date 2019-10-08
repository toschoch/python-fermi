from flask import Blueprint
from flask_restful import Api

from .units import Units
from .questions import RandomFermiQuestions

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

# add resources
api.add_resource(RandomFermiQuestions, '/questions/random')
#api.add_resource(RandomFermiQuestions, '/questions/sources/<string:source>')
#api.add_resource(RandomFermiQuestions, '/categories')
api.add_resource(Units, '/units')
#api.add_resource(RandomFermiQuestions, '/answers')
#api.add_resource(RandomFermiQuestions, '/estimations')