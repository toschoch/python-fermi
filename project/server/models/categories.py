from project.server import db
from project.server.models.base import ModelBase

question_category_assignments_table = \
    db.Table('question_category_assignments', db.Model.metadata,
             db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
             db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
             )


class Category(db.Model, ModelBase):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)

    @classmethod
    def include(cls, c):
        if c in [cls.name]:
            return True
        return False
