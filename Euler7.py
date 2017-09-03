# -*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?

>>> euler(6)
13

>>> euler(10001)
104743
"""
import itertools
from eulerGenerators import primes

def euler(pos):
    return list(itertools.islice(primes(99999999),pos))[pos - 1]

###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")