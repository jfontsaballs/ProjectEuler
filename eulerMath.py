# -*- coding: utf-8 -*-
"""
Math functions
"""

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
    return x == reverse(x)
    
def reverse(x):
    remain = x
    reversed = 0
    while remain > 0:
        reversed = reversed * 10 + remain % 10
        remain = remain // 10
    return reversed
    
    
def lowestCommonMultiple(g)
    for x in g:
        factor(

        
###############################################################################
if __name__ == "__main__":
    import doctest
    fail, total = doctest.testmod()
    if fail == 0:
        print("Tot OK.")        