# -*- coding: utf-8 -*-
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

>>> euler(10)
23

>>> euler(1000)
233168
"""

def euler(maxMultiple):
    return sum(i for i in range(1, maxMultiple) if i % 3 == 0 or i % 5 == 0)

if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")