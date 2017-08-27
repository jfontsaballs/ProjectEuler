# -*- coding: utf-8 -*-
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

>>> euler(4e6)
4613732
"""
from eulerGenerators import fibonacci

def euler(max):
    return sum(i for i in fibonacci(max) if i % 2 == 0)

if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")