# 函数练习 1

"""
    Solve a one-dimensional quadratic equation.
"""

from math import sqrt

a = float(input("Please enter the value of the coefficient a: "))
b = float(input("Please enter the value of the coefficient b: "))
c = float(input("Please enter the value of the coefficient c: "))


def get_solve(a, b, c):
    """
    Two solutions to a quadratic equation are obtained.
    """
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        raise ValueError("get delta under zero.")
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(
            "The two roots of this one-dimensional quadratic equation are: "
            + str(x1)
            + " and "
            + str(x2)
        )
    return x1, x2


try:
    get_solve(a, b, c)
except ValueError as ex:
    print(ex)
