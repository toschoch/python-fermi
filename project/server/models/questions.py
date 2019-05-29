# project/server/models/users.py


import datetime


from project.server import db

class Question(db.Model):

    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(), nullable=False)
    answer = db.Column(db.Float(), nullable=False)
    uncertainty = db.Column(db.Float(), nullable=True)
    creation = db.Column(db.DateTime, nullable=False)
    source = db.Column(db.String(), nullable=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, text, answer, creator_id, uncertainty=None, source=None):
        self.text = text
        self.answer = answer
        self.uncertainty = uncertainty
        self.creation = datetime.datetime.now()
        self.source = source
        self.creator_id = creator_id

    def get_id(self):
        return self.id

    def __str__(self):
        return 'Question: "{:10}..."'.format(self.text)
