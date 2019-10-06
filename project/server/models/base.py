import click
from sqlalchemy.orm.collections import InstrumentedList


class ModelBase:

    @classmethod
    def include(cls, c):
        return True

    def serialize(self):
        return {}

    def as_dict(self):
        d = {}
        for n, c in self.serialize().items():
            if isinstance(c, InstrumentedList):
                d[n] = [e.as_dict() for e in c]
            else:
                d[n] = c.as_dict()
        d.update({c.name: getattr(self, c.name) for c in self.__table__.columns if self.include(c)})
        return d
