'''
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.
'''

from typing import List

arr = [1, 4, 2, 5, 3]

def sumOddLengthSubarrays(arr:List[int]) -> int:
    n, sumOdd = len(arr), 0
    p_sum = [0] * (n + 1)

    for i, a in enumerate(arr):
        p_sum[i + 1]  = p_sum[i] + a

    for i, p in enumerate(p_sum):
        for j in range(i + 1, n + 1, 2):
            sumOdd += p_sum[j] - p_sum[i]
    return sumOdd

print(sumOddLengthSubarrays(arr))
