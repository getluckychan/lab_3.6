from d3 import D3
from sys import getsizeof


class B2(D3):
    def __init__(self, a):
        super().__init__(a)
        self.__a = None

    def show_b2(self):
        self.__a = self.a
        return self.__a, type(self.__a), getsizeof(self.__a)

