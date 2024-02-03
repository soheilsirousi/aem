from Project1 import Statics
from scipy import stats


class T_Distribution:

    def __init__(self):
        self.degrees_of_freedom = list(range(1, 31))
        self.degrees_of_freedom.extend([40, 60, 120])
        self.probability_levels = [0.4, 0.25, 0.1, 0.05, 0.025, 0.01, 0.005, 0.0025, 0.001, 0.005]

    def get(self):
        for x in self.degrees_of_freedom:
            row = list([x])
            for y in self.probability_levels:
                row.append(round(stats.t.ppf(1 - y, x), 3))
            print(row)