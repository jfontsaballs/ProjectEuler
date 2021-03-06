# -*- coding: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

>>> euler(10)
2520

>>> euler(20)
232792560
"""
from eulerMath import lowestCommonMultiple

def euler(maxValue):
    return lowestCommonMultiple(range(2, maxValue + 1))

###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")