from typing import List
'''
Given an unsorted array of integers nums, return the length of the longest 
consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
'''

nums = [100, 4, 200, 1, 3, 2]

def longestConsecutive(nums: List[int]):
    numSet = set(nums)
    longest = 0
    for n in nums:
        # check if it is the start of the sequence
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(longest, length)
    return longest


print(longestConsecutive(nums))