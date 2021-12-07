from sys import getsizeof

class B1:
    def __init__(self, a):
        self.a = a

    def __del__(self):
        return "Викликаний деструктор"

    def show_b1(self):
        return self.a, type(self.a), getsizeof(self.a)

