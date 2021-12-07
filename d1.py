from b1 import B1
from sys import getsizeof


class D1(B1):
    def show_d1(self):
        return self.a, type(self.a), getsizeof(self.a)