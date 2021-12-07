from b1 import B1
from sys import getsizeof


class D2(B1):
    def __init__(self, a):
        super().__init__(a)
        self.__a = None

    def show_d2(self):
        self.__a = self.a
        return self.__a, type(self.__a), getsizeof(self.__a)