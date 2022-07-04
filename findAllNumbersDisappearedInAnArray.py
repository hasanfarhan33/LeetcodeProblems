'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range
[1, n] that do not appear in nums.
'''

from typing import List

nums = [4,3,2,7,8,2,3,1]

def findMissingNumbers(nums: List[int]) -> List[int]:
    size = len(nums)
    numbersSet = set(nums)
    res = []

    for i in range(size):
        if (i + 1) not in numbersSet: res.append(i)

    return res

print(findMissingNumbers(nums))