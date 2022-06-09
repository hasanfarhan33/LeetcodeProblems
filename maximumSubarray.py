'''
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''

from typing import List

nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubarray(nums: List[int]):
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub

print(maxSubarray(nums))