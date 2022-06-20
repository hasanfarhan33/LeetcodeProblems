from typing import List

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

target = 5
nums = [1,3,5,6]

def searchInsert(nums: List[int], target:int) ->int:
    start = 0
    end = len(nums) - 1
    mid = 0

    while start <= end:
        mid = (end + start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid-1
        elif nums[mid] < target:
            start = mid + 1
    return 0

print(searchInsert(nums, target))
