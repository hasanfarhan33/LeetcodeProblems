'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
'''



def mySqrt(x: int) -> int:
    if x == 0: return 0 
    if x == 1: return 1 
    
    l, r = 0, x 
    res = 0 
    
    while l <= r: 
        m = l + ((r - l) // 2)
        if m ** 2 > x: 
            r = m - 1 
        elif m ** 2 < x: 
            l = m + 1 
            res = m 
        else: 
            return m 
    return res 