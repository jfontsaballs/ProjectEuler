# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

>>> euler(100)
9009

>>> euler(1000)
906609
"""
from eulerMath import isPalindrome

def euler(maxValue):
    currentResult = 0
    for i in range(maxValue - 1, 0, -1):
        for j in range(maxValue - 1, 0, -1):
            v = i * j
            if v > currentResult:
                if isPalindrome(v):
                    currentResult = v
            else:
                break
    return currentResult

###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")