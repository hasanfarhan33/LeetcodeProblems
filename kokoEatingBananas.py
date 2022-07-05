'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone
and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and
eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and
will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''

from typing import List
import math

piles = [3, 6, 7, 11]
h = 11

def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    res = right
    while left <= right:
        k = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)

        if hours <= h:
            res = min(res, k)
            right = k - 1
        else:
            left = k + 1
    return res

print(minEatingSpeed(piles, h))
