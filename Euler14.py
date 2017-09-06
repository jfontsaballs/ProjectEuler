# -*- coding: utf-8 -*-
"""
The following iterative sequence is defined for the set of positive integers:

n â†’ n/2 (n is even)
n â†’ 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 â†’ 40 â†’ 20 â†’ 10 â†’ 5 â†’ 16 â†’ 8 â†’ 4 â†’ 2 â†’ 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

>>> euler(1_000_000)
837799
"""
from eulerGenerators import collatz


def euler(maxim):
    llarg = 0
    num = 0
    for i in range (1, maxim):
        l = len(list(collatz(i)))
        if l > llarg:
            llarg = l
            num = i
    return num


###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")