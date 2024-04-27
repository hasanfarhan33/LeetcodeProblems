'''
LEETCODE 1929: Concatenation of Array
'''

from typing import List


def getConcatenation(nums: List[int]) -> List[int]: 
    for n in nums: 
        nums.append(n)
    
    return nums

arr = [1,2,1]

print(getConcatenation(arr))