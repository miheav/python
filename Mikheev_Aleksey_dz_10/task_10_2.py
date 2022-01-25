from abc import ABC, abstractmethod
from math import ceil

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.param) + 0.3)


a = Coat(45)
b = Suit(170)
print(a.calculate)
print(b.calculate)