'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
'''

from typing import List

height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(height: List[int]) -> int:
    if len(height) == 0:
        return 0

    left, right = 0, len(height) - 1
    maxLeft, maxRight = height[left], height[right]
    res = 0

    while left < right:
        if maxLeft < maxRight:
            left+=1
            maxLeft = max(maxLeft, height[left])
            res += maxLeft - height[left]
        else:
            right -= 1
            maxRight = max(maxRight, height[right])
            res += maxRight - height[right]
    return res

print(trap(height))