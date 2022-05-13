'''
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
 not use the same element twice.

You can return the answer in any order.
'''
from typing import List

nums = [3, 2, 4]
target = 6

def twoSum(nums: List[int], target:List[int]):
    hashNumbers = {} #val : index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashNumbers:
            return [hashNumbers[diff], i]
        hashNumbers[num] = i
    return
print(twoSum(nums, target))

