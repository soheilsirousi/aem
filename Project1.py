from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np
from math import comb


class Statics(ABC):
    e = 2.718281828459045
    pi = 3.14159265358979

    @classmethod
    def fact(cls, number):
        if number == 0:
            return 1
        fact = 1
        for i in range(number, 0, -1):
            fact *= number
            number -= 1

        return fact


    @abstractmethod
    def draw_diagram(self):
        pass


class Poisson(Statics):

    def __init__(self, miu=0, r=range(0, 15)):
        self.miu = miu
        self.r = r
        self.result = dict()

    def get_pmf(self):
        for i in self.r:
            self.result[i] = self.pmf(i)

        return self.result

    def pmf(self, r):
        return (self.e**(-1*(self.miu))*(self.miu**r))/self.fact(r)


    def get_input(self):
        miu = float(input('Enter the μ: '))
        r_start = int(input('Enter the start range: '))
        r_end = int(input('Enter the end range: '))
        self.miu = miu
        self.r = range(r_start, r_end)

    def draw_diagram(self):
        plt.bar(list(self.result.keys()), list(self.result.values()), color='red', alpha=0.7, label='Poisson PMF')

        plt.title(f'Poisson distribution with {self.miu}')
        plt.xlabel('The number of occurrences of events')
        plt.ylabel('Possibility')
        plt.legend()
        plt.show()


class Bernoulli(Statics):

    def __init__(self, n=14, p=0):
        self.n = n
        self.r = range(0, n+1)
        self.p = p
        self.q = 1 - p
        self.result = dict()

    def get_pmf(self):
        for i in self.r:
            self.result[i] = self.pmf(i)

        return self.result

    def pmf(self, r):
        return (comb(self.n, r)*self.p**r*self.q**(self.n-r))

    def get_input(self):
        n = int(input('Enter the number of experiment: '))
        p = float(input('Enter the success possibility: '))
        self.n = n
        self.r = range(0, n + 1)
        self.p = p
        self.q = 1 - p

    def draw_diagram(self):
        plt.bar(list(self.result.keys()), list(self.result.values()), color='red', alpha=0.7, label='Bernoulli PMF')

        plt.title(f'Bernoulli distribution with {self.n} experiment & possibility {self.p}')
        plt.xlabel('Success number')
        plt.ylabel('Possibility')
        plt.legend()
        plt.show()


class NBinom(Statics):

    def __init__(self, r=0, p=0, k=range(0, 15)):
        self.r = r
        self.k = k
        self.p = p
        self.q = 1 - p
        self.result = dict()

    def get_pmf(self):
        for i in self.k:
            self.result[i] = self.pmf(i)

        return self.result

    def pmf(self, k):
        return (comb(k+self.r-1, k) * self.p**self.r * (1-self.p)**k)

    def get_input(self):
        r = int(input('Enter the number of success: '))
        p = float(input('Enter the success possibility: '))
        k = int(input('Enter the number of experiment before success: '))
        self.r = r
        self.k = range(0, k)
        self.p = p
        self.q = 1 - p

    def draw_diagram(self):
        plt.bar(list(self.result.keys()), list(self.result.values()), color='red', alpha=0.7, label='Negative Binom PMF')

        plt.title(f'Negative Binom distribution with {self.r} success & possibility {self.p}')
        plt.xlabel('Success number')
        plt.ylabel('Possibility')
        plt.legend()
        plt.show()


class MultiNomial(Statics):

    def __init__(self, n=0, k=0, p=[]):
        self.n = n
        self.k = k
        self.p = p
        self.x = range(0, n+1)
        self.result = dict()

    def get_pmf(self):
        for x in self.x:
            self.result[x] = self.pmf([x, self.n-x, 0])

        return self.result

    def pmf(self, x):
        rst = self.fact(self.n) / np.prod([self.fact(xi) for xi in x])
        return rst * np.prod([p ** xi for p, xi in zip(self.p, x)])

    def get_input(self):
        k = int(input('Enter the number of categories: '))
        n = int(input('Enter the number of experiments: '))
        for i in range(k):
            p = float(input(f'Enter the {i+1} experiment success possible: '))
            self.p.append(p)
        self.n = n
        self.k = k
        self.x = range(0, n + 1)

    def draw_diagram(self):
        plt.bar(list(self.result.keys()), list(self.result.values()), color='red', alpha=0.7, label='Multi Nomial PMF')

        plt.title(f'Multi Nomial distribution with {self.n} experiment')
        plt.xlabel('Number of success in each cat')
        plt.ylabel('Possibility')
        plt.legend()
        plt.show()


class Geometric(Statics):

    def __init__(self, p=0, k=range(1, 11)):
        self.p = p
        self.q = 1 - p
        self.k = k
        self.result = dict()

    def get_pmf(self):
        for i in self.k:
            self.result[i] = self.pmf(i)

        return self.result

    def pmf(self, i):
        return self.p*self.q**(i-1)

    def get_input(self):
        p = float(input('Enter the possibility: '))
        k_end = int(input('Enter the number of experiments: '))
        self.p = p
        self.q = 1 - p
        self.k = range(1, k_end+1)

    def draw_diagram(self):
        plt.bar(list(self.result.keys()), list(self.result.values()), color='red', alpha=0.7, label='Geometric PMF')

        plt.title(f'Geometric distribution with {self.p} possibility')
        plt.xlabel('Number of experiments')
        plt.ylabel('Possibility')
        plt.legend()
        plt.show()
