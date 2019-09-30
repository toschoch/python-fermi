import datetime

from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
  "Add support for serializing timedeltas"

  def default(self, o):
    if type(o) == datetime.timedelta:
      return str(o)
    else:
      return super().default(o)
