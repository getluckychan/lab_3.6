from d1 import D1
from d2 import D2
from sys import getsizeof


class D3(D1, D2):
    def show_d3(self):
        return self.a, type(self.a), getsizeof(self.a)