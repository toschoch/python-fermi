from project.server import db
from project.server.models import User
from project.server.models.base import ModelBase
from project.server.models.categories import Category, question_category_assignments_table
from project.server.models.datasources import DataSource
from project.server.models.units import Unit


class Question(ModelBase, db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(), nullable=False)
    answer = db.Column(db.Float(), nullable=False)
    creation = db.Column(db.DateTime, nullable=False)

    uncertainty = db.Column(db.Float(), nullable=True)
    reference = db.Column(db.String(), nullable=True)

    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    creator = db.relationship(User)

    source_id = db.Column(db.Integer, db.ForeignKey('datasources.id'), nullable=False)
    source = db.relationship(DataSource)

    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False)
    unit = db.relationship(Unit)

    categories = db.relationship(Category, secondary=question_category_assignments_table)

    @classmethod
    def include(cls, c):
        if c in [cls.id, cls.creator_id, cls.source_id, cls.unit_id]:
            return False
        return True

    #def serialize(self):
     #   return {"unit": self.unit, "source": self.source, "categories": self.categories}

    def get_id(self):
        return self.id

