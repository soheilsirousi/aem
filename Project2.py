from math import sqrt
import matplotlib.pyplot as plt
from scipy import stats
from Project1 import Statics
import numpy as np


class NormalDistribution(Statics):

    def __init__(self, *args, **kwargs):
        self.mu = 0
        self.sigma = 0
        self.range = None
        super().__init__(*args, **kwargs)


    def function(self, x):
        return (1/(self.sigma*sqrt(2*self.pi)))*self.e**((-1/2)*(((x - self.mu)/self.sigma)**2))


    def get_pmf(self):
        self.result = dict()
        for x in self.range:
            self.result[x] = self.function(x)

        return self.result


    def input_user(self):
        self.mu = float(input('Enter the mu value: '))
        self.sigma = float(input('Enter the sigma value: '))
        start = int(input('Enter the start: '))
        end = int(input('Enter the end point: '))
        self.range = range(start, end)


    def draw_diagram(self):
        plt.plot(list(self.result.keys()), list(self.result.values()), color='red', alpha=0.7, label='Normal Distribution PMF')

        plt.title(f'Normal Distribution with {self.mu}, {self.sigma}')
        plt.xlabel('x')
        plt.ylabel('Probability')
        plt.legend()
        plt.show()


class TDistribution:

     def __init__(self):
         self.x = np.linspace(-4, 4, 1000)
         self.degrees_of_freedom = list()

     def input_user(self):
        degrees_of_freedom = input('Enter the degress of freedom (Seprated by white space): ')
        degrees_of_freedom = degrees_of_freedom.split()
        for deg in degrees_of_freedom:
            self.degrees_of_freedom.append(int(deg))

     def draw_diagram(self):
         for df in self.degrees_of_freedom:
            plt.plot(self.x, stats.t.pdf(self.x, df),
                    label=f'df = {df}')
         plt.title('TStudent Distribution PMF')
         plt.xlabel('x')
         plt.ylabel('Probability')
         plt.legend()
         plt.show()
