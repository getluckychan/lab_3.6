from sys import getsizeof
from b1 import B1
from d1 import D1
from d2 import D2
from d3 import D3
from b2 import B2


def main():
    a = B1(1)
    print(getsizeof(B1), "\nІєрархія класу B1: ", a.show_b1())
    a1 = D1(2)
    print(getsizeof(D1), "\nІєрархія класу D1: ", a1.show_d1())
    a2 = D2(3)
    print(getsizeof(D2), "\nІєрархія класу D2: ", a2.show_d2())
    a3 = D3(4)
    print(getsizeof(D3), "\nІєрархія класу D3: ", a3.show_d3())
    a4 = B2(5)
    print(getsizeof(B2), "\nІєрархія класу B2: ", a4.show_b2())


main()
