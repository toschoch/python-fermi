# project/server/models/users.py


import datetime

from project.server import db
from project.server.models.base import ModelBase


class Question(ModelBase, db.Model):
    __tablename__ = "questions"

    id: int
    text: str
    answer: float
    uncertainty: float
    creation: datetime.datetime
    source: str
    creator_id: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(), nullable=False)
    answer = db.Column(db.Float(), nullable=False)
    unit = db.Column(db.String(), nullable=False)
    uncertainty = db.Column(db.Float(), nullable=True)
    creation = db.Column(db.DateTime, nullable=False)
    source = db.Column(db.String(), nullable=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @classmethod
    def serialize(cls, c):
        if c in [cls.id, cls.creator_id]: return False
        return True

    def get_id(self):
        return self.id
