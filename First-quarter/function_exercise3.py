# 函数练习 3

"""
    找出 100 以内的素数
"""
import math


def is_prime(num):
    """
    Determining whether a natural number is prime.
    """
    if num <= 1:
        return False
    up_sqrt = int(math.sqrt(num) + 1)
    for i in range(2, int(up_sqrt)):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print([i for i in range(2, 100) if is_prime(i)])
