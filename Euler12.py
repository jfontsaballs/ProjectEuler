# -*- coding: utf-8 -*-
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

>>> euler(5)
28

>>> euler(500)
76576500
"""
from eulerGenerators import triangleNumbers, allFactors

def euler(maxim):
    for i in triangleNumbers(maxim ** maxim):
        if len(list(allFactors(i))) >= maxim:
            return i


###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")