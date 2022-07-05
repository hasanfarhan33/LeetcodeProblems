'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

from typing import List

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

def search(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if not nums[i - 1] or nums[i - 1] != nums[i] - 1: # Start of a sequence
            left = i
        if not nums[i + 1] or nums[i + 1] != nums[i] + 1: # End of a sequence
            right = i

        if target == nums[left]: return left
        elif target == nums[right]: return right

        if target > nums[left] and target < nums[right]:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else: return mid
    return -1


