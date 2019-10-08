import logging
from io import StringIO

import requests
import pandas as pd
import numpy as np

log = logging.getLogger(__name__)


class WikiDataClient:
    URL = 'https://query.wikidata.org/sparql'

    @classmethod
    def query(cls, query_text):
        r = requests.get(cls.URL, params={'format': 'json', 'query': query_text})
        data = r.json()
        bindings = data['results']['bindings']
        datetime_columns = [c for row in bindings for c in row.keys() if row[c].get('datatype','').split('#')[-1]=='dateTime']
        datetime_columns = np.unique(datetime_columns).tolist()
        data = pd.DataFrame.from_dict(map(lambda row: {k: row[k]["value"] for k in row.keys()}, bindings))
        io = StringIO()
        requested_vars = r.json()['head']['vars']
        data[data.columns.intersection(requested_vars)].to_csv(io,index=False)
        io.seek(0)
        if len(datetime_columns) > 0:
            return pd.read_csv(io, parse_dates=datetime_columns)
        else:
            return pd.read_csv(io)
