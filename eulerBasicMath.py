# -*- coding: utf-8 -*-
"""
Reimplementation of basic math functions
"""
from eulerExceptions import ArgumentMustBeNonNegative


def abs(x):
    """
    >>> abs(-3)
    3
    >>> abs(4.2)
    4.2
    >>> abs(0)
    0
    """
    return x if x >= 0 else -x


def squareRoot(x, precision):
    """
    >>> squareRoot(4, 0.01)
    2.0
    >>> abs(squareRoot(5, 0.00001) - 2.23606798) < 0.0001
    True
    >>> squareRoot(-4, 0.01)
    Traceback (most recent call last):
        ...
    eulerExceptions.ArgumentMustBeNonNegative: Square root can only be computed on positive values
    """
    
    if x < 0:
        raise ArgumentMustBeNonNegative("Square root can only be computed on positive values")
    
    r = x/2
    previousR = r + 2 * precision
    while abs(previousR - r) > precision:
        previousR = r
        r = (r * r + x) / (2 * r)
    return r
    
    
###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")