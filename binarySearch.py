from typing import List

nums = [-1, 0, 3, 5, 9, 12]
target = 9

def binarySearch(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else: return mid
    return -1

print(binarySearch(nums, target))