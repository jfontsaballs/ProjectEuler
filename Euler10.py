# -*- coding: utf-8 -*-
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

>>> euler(10)
17

>>> euler(2_000_000)
142913828922
"""
from eulerGenerators import primes

def euler(maxim):
    return sum(primes(maxim - 1))


###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")