'''
LEETCODE 2441
'''

from typing import List


arr = [-1,10,6,7,-7,1]

def findMax(nums: List[int])-> int: 
    nums.sort() 
    left, right = 0, len(nums) - 1
    max_num = -1 
    while left < right: 
        if nums[left] + nums[right] == 0: 
            max_num = max(max_num, nums[right])
        elif nums[left] + nums[right] < 0: 
            left += 1 
        elif nums[left] + nums[right] > 0: 
            right -= 1
    return max_num if max_num != float('-inf') else -1 

print(findMax(arr))