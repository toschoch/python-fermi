from project.server import db
from project.server.models.base import ModelBase


class DataSource(db.Model, ModelBase):
    __tablename__ = "datasources"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)

    @classmethod
    def include(cls, c):
        if c in [cls.name]:
            return True
        return False