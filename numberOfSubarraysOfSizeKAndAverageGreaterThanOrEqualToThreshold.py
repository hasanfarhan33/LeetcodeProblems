'''
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average
greater than or equal to threshold.
'''

from typing import List

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

def numOfSubarrays(arr:List[int], k:int, threshold:int) -> int:
    res = left = curSum = 0
    for right in range(len(arr)):
        curSum += arr[right]
        if right - left + 1 == k:
            curAv = curSum // k
            curSum -= arr[left]
            left += 1
            if curAv >= threshold:
                res+=1
    return res

print(numOfSubarrays(arr, k, threshold))