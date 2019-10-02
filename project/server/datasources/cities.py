import datetime
import random
import requests

from project.server.datasources.base import BaseSource
from project.server.models import Question


class Cities(BaseSource):

    @classmethod
    def get_country(cls):
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
        return countries[random.randint(0, len(countries) - 1)].split("/")[-1]

    @classmethod
    def get_question(cls):
        country = Cities.get_country()
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

        q = Question(text="What is the {} of {} (in {})?".format(
            statement["propertyLabel"]["value"],
            statement["itemLabel"]["value"]),
            source="www.wikidata.org",
            creation=datetime.now(),
            unit=statement["unitLabel"]["value"],
            answer=float(statement["value"]["value"]))

        return q

    @classmethod
    def questions_count(cls):
        return 1000

    @classmethod
    def questions_weight(cls):
        return 0.00