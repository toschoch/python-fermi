from project.server import db
from project.server.models.base import ModelBase


class Unit(db.Model, ModelBase):
    __tablename__ = "units"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.String(), nullable=True)
    formula = db.Column(db.String(), nullable=True)
    shortFormula = db.Column(db.String(), nullable=True)
    latex = db.Column(db.String(), nullable=True)
    wikidata = db.Column(db.String(), nullable=True)


    @classmethod
    def include(cls, c):
        if c in [cls.name]:
            return True
        return False
