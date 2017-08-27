# -*- coding: utf-8 -*-
"""
Iterator functions for generating series of numbers
"""
from eulerBasicMath import squareRoot
from eulerExceptions import ArgumentMustBeNonNegativeInteger
import numbers


def fibonacci(max):
    """
    >>> list(fibonacci(60))
    [1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    a = 1
    b = 1
    while b < max:
        yield b
        a, b = b, a + b

		
###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")
