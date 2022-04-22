'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer
array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.
'''
from typing import List

numbers = [2,3,4]
target = 6

# BRUTE FORCE SOLUTION
def twoSumBruteForce(numbers:List[int], target:int):
    res = []
    for i in range(len(numbers) - 1):
        for j in range(len(numbers)):
            if j == i:
                j+=1
            else:
                if numbers[i] + numbers[j] == target:
                    res.append(i + 1)
                    res.append(j + 1)
                    return res



def twoSum(numbers:List[int], target:int):
    left = 0
    right = len(numbers) - 1
    while left < right:
        currentSum = numbers[left] + numbers[right]
        if currentSum > target:
            right -= 1
        elif currentSum < target:
            left += 1
        else:
            return [left + 1, right + 1]
    return []



print(twoSum(numbers, target))
# print(twoSum(numbers, target))

