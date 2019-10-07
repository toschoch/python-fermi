import logging
from io import StringIO

import requests
import pandas as pd

log = logging.getLogger(__name__)


class WikiDataClient:
    URL = 'https://query.wikidata.org/sparql'

    @classmethod
    def query(cls, query_text):
        r = requests.get(cls.URL, params={'format': 'json', 'query': query_text})
        data = r.json()
        bindings = data['results']['bindings']
        data = pd.DataFrame.from_dict(map(lambda row: {k: row[k]["value"] for k in row.keys()}, bindings))
        io = StringIO()
        data[r.json()['head']['vars']].to_csv(io,index=False)
        io.seek(0)
        return pd.read_csv(io)
