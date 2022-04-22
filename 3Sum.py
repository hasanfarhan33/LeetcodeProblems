'''
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
from typing import List

nums = [-1, 0, 1, 2, -1, -4]

def threeSum(nums:List[int]) -> List[List[int]]:
    k = 0
    left = 0
    right = len(nums) - 1
    sortedNums = sorted(nums)
    res = []
    for k in range(len(sortedNums)):
        while left < right:
            if left == k:
                left+=1
            if right == k:
                right -= 1
            sum = sortedNums[left] + sortedNums[right]
            if sum < k:
                left += 1
            elif sum > k:
                right -= 1
            else:
                res.append([sortedNums[left], sortedNums[right], sortedNums[k]])
    return(res)

def threeSumBetterSolution(nums:List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        left, right = i+1, len(nums) -1
        while left < right:
            threeSum = a + nums[left] + nums[right]
            if threeSum > 0:
                right-=1
            elif threeSum < 0:
                left+=1
            else:
                res.append([a, nums[left], nums[right]])
                left+=1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res

print(threeSum(nums))