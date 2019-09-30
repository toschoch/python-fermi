class ModelBase:

    @classmethod
    def serialize(cls, c):
        return True

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if self.serialize(c)}