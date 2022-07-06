'''
Let's call an array arr a mountain if the following properties hold:

   * arr.length >= 3
   * There exists some i with 0 < i < arr.length - 1 such that:
       - arr[0] < arr[1] < ... arr[i-1] < arr[i]
       - arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array arr that is guaranteed to be a mountain, return any i
such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
'''

from typing import List

arr = [3,9,8,6,4]

def peakIndex(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]: return mid
        if arr[mid - 1] > arr[mid]: right = mid
        elif arr[mid + 1] > arr[mid]: left = mid + 1
    return -1

print(peakIndex(arr))
