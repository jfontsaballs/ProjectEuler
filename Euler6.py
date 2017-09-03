# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

>>> euler(10)
2640

>>> euler(100)
25164150
"""

def euler(maxValue):
    return (sum(range(1, maxValue + 1)) ** 2) - (sum(map(lambda x: x ** 2, range(1, maxValue + 1))))

###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")