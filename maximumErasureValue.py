'''
You are given an array of positive integers nums and want to erase a
subarray containing unique elements. The score you get by erasing the
subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.
'''

from typing import List

nums = [4, 2, 4, 5, 6]

def maximumUniqueSubarray(nums: List[int]) -> int:
    left, right, seen, arrSize, curSum = 0, 0, set(), len(nums), 0
    maxSum = 0

    while right < arrSize:
        if nums[right] not in seen:
            curSum += nums[right]
            seen.add(nums[right])
            right += 1
            maxSum = max(maxSum, curSum)
        else:
            curSum -= nums[left]
            seen.remove(nums[left])
            left += 1
    return maxSum


print(maximumUniqueSubarray(nums))