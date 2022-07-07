'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result
should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

   * |a - x| < |b - x|, or
   * |a - x| == |b - x| and a < b
'''

from typing import List

arr = [1,2,3,4,5]
k = 4
x = 3

def kClosestElements(arr:List[int], k:int, x:int)->List[int]:
    if x <= arr[0]: return arr[:k]
    if x >= arr[-1]: return arr[-k:]

    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left : left + k]
# print(kClosestElements(arr, k, x))
print(ord('a'))
print(ord('b'))