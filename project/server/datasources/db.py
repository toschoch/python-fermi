from sqlalchemy import func

from project.server.datasources.base import BaseSource
from project.server.models import Question


class SqlDataBaseSource(BaseSource):

    @classmethod
    def get_question(cls):
        question = Question.query.order_by(func.random()).limit(1).first()
        return question

    @classmethod
    def questions_count(cls):
        return Question.query.count()