# -*- coding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

>>> euler(13195)
29
>>> euler(600851475143)
6857
"""
from eulerGenerators import factor

def euler(max):
    return list(factor(max))[-1]

###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")