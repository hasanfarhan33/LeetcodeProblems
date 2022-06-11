'''
You are given an integer array nums and an integer x. In one operation, you can either remove
the leftmost or the rightmost element from the array nums and subtract its value from x.
Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible,
otherwise, return -1.
'''

from typing import List

x = 5
nums = [1, 1, 4, 2, 3]

def minOperations(nums: List[int]):
    if len(nums) == 1 and nums[0] == x:
        return 1
    elif len(nums) == 1 and nums[0] != x:
        return -1

    leftPointer = 0
    rightPointer = leftPointer + 1
    total, counter = 0, 0

    while leftPointer < rightPointer and rightPointer < len(nums) - 1:
        if nums[leftPointer] or nums[rightPointer] == x:
            return 1

        total = nums[leftPointer] + nums[rightPointer]
        counter = 2

        if total == x:
            return counter
        if total < x:
            rightPointer += 1
            sum += nums[rightPointer]
            couter += 1

        if total > x:
            total -= nums[leftPointer]
            leftPointer += 1
            counter -= 1

def minOperationsBetter(nums: List[int], x: int):
    totalSum = sum(nums)
    if totalSum < x:
        return -1
    elif totalSum == x:
        return len(nums)

    midArraySum = totalSum - x
    left = 0
    midArraySize = currentSum = 0

    for right, num in enumerate(nums):
        currentSum += num
        if currentSum > midArraySum:
            currentSum -= nums[left]
            left += 1
        if currentSum == midArraySum:
            midArraySize = max(midArraySize, right - left + 1)
    if midArraySize == 0:
        return -1
    else:
        return len(nums) - midArraySize

print(minOperationsBetter(nums, x))