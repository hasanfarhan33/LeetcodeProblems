'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
from typing import List

nums = [4,1,2,1,2]

def singleNumber(nums:List[int]) -> int:
    seen = set()
    for n in nums:
        if n not in seen:
            seen.add(n)
        else: seen.remove(n)
    return seen.pop()

print(singleNumber(nums))
