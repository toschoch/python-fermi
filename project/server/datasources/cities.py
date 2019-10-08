import datetime
import random
import requests

from .base import BaseSource
from project.server.models import Question
from .countries import Countries


class Cities(BaseSource):

    @classmethod
    def get_question(cls):

        url = 'https://query.wikidata.org/sparql'

        country1, country2 = Countries.get_countries(2)

        cities = """
SELECT ?city1Label ?pop1 ?city2Label ?pop2 ?dist
WHERE
{
  ?city1 wdt:P17 wd:""" +country1+ """.
  ?city1 wdt:P31 wd:Q515.
  ?city1 wdt:P1082 ?pop1.
  ?city2 wdt:P17 wd:""" +country2+ """.
  ?city2 wdt:P31 wd:Q515.
  ?city2 wdt:P1082 ?pop2.
  
  ?city1 wdt:P625 ?loc1.
  ?city2 wdt:P625 ?loc2.
  
  BIND(geof:distance(?loc1, ?loc2) as ?dist) 
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
} 
"""
        r = requests.get(url, params={'format': 'json', 'query': cities})
        data = r.json()
        distances = data['results']['bindings']
        distance = distances[random.randint(0, len(distances))]

        q = Question(text="What is the distance from {} to {} ({})?".format(
            distance["city1Label"]["value"], distance["city2Label"]["value"]),
            source="www.wikidata.org",
            creation=datetime.now(),
            answer=distance["dist?"]["value"],
            uncertainty=distance["dist?"]["value"] * 0.2 ,
            unit='kilometer')
        return q

    @classmethod
    def questions_count(cls):
        return 1000

    @classmethod
    def questions_weight(cls):
        return 0