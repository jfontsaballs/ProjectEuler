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

    >>> list(allFactors(64))
    [1, 2, 4, 8, 16, 32]

    >>> list(allFactors(1_000_000_000))
    [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80, 100, 125, 128, 160, 200, 250, 256, 320, 400, 500, 512, 625, 640, 800, 1000, 1250, 1280, 1600, 2000, 2500, 2560, 3125, 3200, 4000, 5000, 6250, 6400, 8000, 10000, 12500, 12800, 15625, 16000, 20000, 25000, 31250, 32000, 40000, 50000, 62500, 64000, 78125, 80000, 100000, 125000, 156250, 160000, 200000, 250000, 312500, 320000, 390625, 400000, 500000, 625000, 781250, 800000, 1000000, 1250000, 1562500, 1600000, 1953125, 2000000, 2500000, 3125000, 3906250, 4000000, 5000000, 6250000, 7812500, 8000000, 10000000, 12500000, 15625000, 20000000, 25000000, 31250000, 40000000, 50000000, 62500000, 100000000, 125000000, 200000000, 250000000, 500000000]
    """
    bigFactors = []
    yield 1
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            lastBigFactor = x // i
            if i > lastBigFactor:
                break
            bigFactors.append(lastBigFactor)
            if i == lastBigFactor:
                break
            yield i
    for i in reversed(bigFactors):
        yield i


###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")
