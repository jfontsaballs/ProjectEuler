# -*- coding: utf-8 -*-
"""
Math functions
"""
from functools import reduce
from eulerGenerators import factor

def isPalindrome(x):
    """
    >>> isPalindrome(9449)
    True
    >>> isPalindrome(70107)
    True
    >>> isPalindrome(5005)
    True
    >>> isPalindrome(1041)
    False
    >>> isPalindrome(350503)
    False
    """
    return x == _reverse(x)

def _reverse(x):
    remain = x
    reversed = 0
    while remain > 0:
        reversed = reversed * 10 + remain % 10
        remain = remain // 10
    return reversed


def lowestCommonMultiple(numbers):
    """
    >>> lowestCommonMultiple([20, 30])
    60
    >>> lowestCommonMultiple([35, 41, 14])
    2870
    """
    factors = []
    for x in numbers:
        factors = _combineFactors(factors, factor(x))
    return reduce(lambda x, y: x * y, factors)

def _combineFactors(a, b):
    if a and b:
        temp = list(b)
        for x in a:
            try:
                temp.remove(x)
            except ValueError:
                pass
        return list(a) + temp
    else:
        return list(a or b)


###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")