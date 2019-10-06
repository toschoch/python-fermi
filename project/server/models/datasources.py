from project.server import db


class DataSource(db.Model):
    __tablename__ = "datasources"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)