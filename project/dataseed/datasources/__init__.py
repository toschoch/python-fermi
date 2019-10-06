import random
import numpy as np

from project.dataseed.datasources.cities import Cities
from project.dataseed.datasources.countries import Countries
from project.dataseed.datasources.db import SqlDataBaseSource


class AllSources:


    @staticmethod
    def get_question():

        sources = [Countries, SqlDataBaseSource, Cities]
        source_counts = np.array([src.questions_count() for src in sources])
        source_weights = np.array([src.questions_weight() for src in sources])
        source_counts = source_counts * source_weights
        source_shares = np.cumsum(source_counts)
        source_shares = source_shares / source_shares[-1]

        sample = random.random()
        i = source_shares[source_shares > sample].tolist().index(True) - 1
        return sources[i].get_question()
