from datetime import datetime
import random
import numpy as np
import requests

from project.dataseed.datasources.base import BaseSource
from project.server.models import Question


class Countries(BaseSource):

    @classmethod
    def get_countries(cls, n=1):
        url = 'https://query.wikidata.org/sparql'

        q = """
SELECT ?item
WHERE
{
  ?item wdt:P31 wd:Q6256.
} 
"""
        r = requests.get(url, params={'format': 'json', 'query': q})
        countries = list(map(lambda x: x['item']['value'], r.json()['results']['bindings']))
        return [c.split("/")[-1] for c in np.random.choice(np.array(countries), n, replace=True)]

    @classmethod
    def get_question(cls):
        country = Countries.get_countries()[0]
        url = 'https://query.wikidata.org/sparql'
        query = """
SELECT ?itemLabel ?item ?propertyLabel  ?lowerBound ?value ?valuePred ?upperBound ?unitLabel ?statement
WHERE
{
  wd:""" + country + """  ?predicate                  ?statement.
  ?item          ?predicate                  ?statement.
  ?property      wikibase:claim              ?predicate.
  ?property      wikibase:statementValue     ?valuePred.
  ?statement     ?valuePred                  ?valueNode.
  ?valueNode     wikibase:quantityAmount     ?value.
  ?valueNode     wikibase:quantityUnit       ?unit.
  ?statement     wikibase:rank               ?rank.

  FILTER(?rank != wikibase:DeprecatedRank)

  OPTIONAL {
          ?valueNode  wikibase:quantityLowerBound ?lowerBound.
          ?valueNode  wikibase:quantityUpperBound ?upperBound.
  }

  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
"""
        r = requests.get(url, params={'format': 'json', 'query': query})
        data = r.json()
        statements = data['results']['bindings']
        statement = statements[random.randint(0, len(statements) - 1)]

        value = float(statement["value"]["value"])
        try:
            uncertainty = float(statement["upperBound"]["value"]) - float(statement["lowerBound"]["value"])
        except:
            uncertainty = value * 0.2  # 20% is standard uncertainty

        q = Question(text="What is the {} of {} ({})?".format(
            statement["propertyLabel"]["value"],
            statement["itemLabel"]["value"], statement["statement"]["value"]),
            source="www.wikidata.org",
            creation=datetime.now(),
            unit=statement["unitLabel"]["value"],
            uncertainty=uncertainty,
            answer=value)
        return q

    @classmethod
    def questions_count(cls):
        return 1000

    @classmethod
    def questions_weight(cls):
        return 0.05
