from flask import jsonify
from flask_restful import Resource
from sqlalchemy import func

from project.server.models import Unit

import logging

log = logging.getLogger(__name__)


class Units(Resource):

    @staticmethod
    def get():
        units = Unit.query.all()

        return jsonify([u.as_dict() for u in units])
