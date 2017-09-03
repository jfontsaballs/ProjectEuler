# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?

>>> euler(3 + 4 + 5)
60

>>> euler(1000)
31875000
"""

def euler(maxim):
    for a in range(1, maxim + 1):
        for b in range(1, maxim + 1 - a):
            c = maxim - a - b
            if a ** 2 + b ** 2 == c ** 2:
                break
        else:
            continue
        break
    else:
        raise Exception("No hi ha cap combinació")
    return a * b * c


###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")