'''
Leetcode 169 
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

from typing import List


def majorityElement(nums: List[int]) -> int: 
    seen_nums = {}
    n = len(nums) 
    for num in nums: 
        seen_nums[num] = seen_nums.get(num, 0) + 1
        if seen_nums[num] > n / 2: 
            return num 


print(majorityElement([3,3,2]))