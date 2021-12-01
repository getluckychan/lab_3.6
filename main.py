from sys import getsizeof


class B1:
    def __init__(self, a):
        self.a = a

    def show_b1(self):
        return self.a, type(self.a), getsizeof(self.a)


class D1(B1):
    def show_d1(self):
        return self.a, type(self.a), getsizeof(self.a)


class D2(B1):
    def __init__(self, a):
        super().__init__(a)
        self.__a = None

    def show_d2(self):
        self.__a = self.a
        return self.__a, type(self.__a), getsizeof(self.__a)


class D3(D1, D2):
    def show_d3(self):
        return self.a, type(self.a), getsizeof(self.a)


class B2(D3):
    def __init__(self, a):
        super().__init__(a)
        self.__a = None

    def show_b2(self):
        self.__a = self.a
        return self.__a, type(self.__a), getsizeof(self.__a)


def main():
    a = B1(1)
    print(getsizeof(B1), "\nІєрархія класу B1: ", a.show_b1())
    a1 = D1(1)
    print(getsizeof(D1), "\nІєрархія класу D1: ", a1.show_d1())
    a2 = D2(1)
    print(getsizeof(D2), "\nІєрархія класу D2: ", a2.show_d2())
    a3 = D3(1)
    print(getsizeof(D3), "\nІєрархія класу D3: ", a3.show_d3())
    a4 = B2(1)
    print(getsizeof(B2), "\nІєрархія класу B2: ", a4.show_b2())


main()
