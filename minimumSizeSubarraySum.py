'''
Given an array of positive integers nums and a positive integer target, return the minimal length
of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than
or equal to target. If there is no such subarray, return 0 instead.
'''

from typing import List

# This is a sliding window problem
nums = [2, 3, 1, 2, 4, 3]
target = 7

def minSubArrayLen(target:int, nums:List[int]) -> int:
    total = left = 0
    minLen = len(nums) + 1

    for right, n in enumerate(nums):
        total += n
        while total >= target:
            minLen = min(minLen, right - left + 1)
            total -= nums[left]
            left += 1
    return minLen if minLen <= len(nums) else 0

print(minSubArrayLen(target, nums))
