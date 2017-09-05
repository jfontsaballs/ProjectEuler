# -*- coding: utf-8 -*-
"""
Iterator functions for generating series of numbers
"""
from eulerBasicMath import intSquareRoot
from eulerExceptions import ArgumentMustBeNonNegativeInteger
from timeit import timeit
import numbers

def fibonacci(maximum):
    """
    >>> list(fibonacci(60))
    [1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    a = 1
    b = 1
    while b < maximum:
        yield b
        a, b = b, a + b

def triangleNumbers(maximum):
    """
    >>> list(triangleNumbers(10))
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    """
    sum = 0
    for i in range(1, maximum + 1):
        sum += i
        yield sum

def primes(maximum):
    """
    >>> list(primes(1000.0))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    >>> list(primes(17))
    [2, 3, 5, 7, 11, 13, 17]
    """
    primes = [3, 5, 7]
    yield 2
    yield 3
    yield 5
    yield 7
    for candidate in range(12, int(maximum) + 10, 6):
        nextCandidate = candidate - 1
        if nextCandidate > maximum:
            break
        if _testCandidate(nextCandidate, primes):
            primes.append(nextCandidate)
            yield nextCandidate

        nextCandidate = candidate + 1
        if nextCandidate > maximum:
            break
        if _testCandidate(nextCandidate, primes):
            primes.append(nextCandidate)
            yield nextCandidate

def _testCandidate(candidate, primes):
    squareRoot = intSquareRoot(candidate)
    for prime in primes:
        if candidate % prime == 0:
            return 0
        elif prime > squareRoot:
            return candidate
    else:
        return candidate


def factor(x):
    """
    >>> list(factor(60))
    [2, 2, 3, 5]
    >>> list(factor(2244))
    [2, 2, 3, 11, 17]
    >>> list(factor(70554))
    [2, 3, 11, 1069]
    >>> list(factor(14))
    [2, 7]
    >>> list(factor(9.3))
    Traceback (most recent call last):
        ...
    eulerExceptions.ArgumentMustBeNonNegativeInteger: Only positive integers can be factored
    """
    if not isinstance(x, numbers.Integral):
        raise ArgumentMustBeNonNegativeInteger("Only positive integers can be factored")

    remain = x
    for p in primes(x / 2):
        while remain % p == 0:
            yield p
            remain = remain // p
        if remain == 1:
            break
    else:
        yield x


def allFactors(x):
    """
    >>> list(allFactors(60))
    [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30]
    """
    for i in range(1, int(x / 2) + 1):
        if x % i == 0:
            yield i

###############################################################################
if __name__ == "__main__":
    #import datetime
    #d=datetime.datetime.now()
    #list(primes(1000_000))
    #print(datetime.datetime.now() - d)
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")
