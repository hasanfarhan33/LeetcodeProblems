'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

from typing import List

nums = [3, 2, 1, 5, 6, 4]
k = 2 # Second Largest Element

def kthLargestElement(nums:List[int], k:int) -> int:
    kIndex = len(nums) - k # Index of the kth largest element if the array was sorted
    # Quickselect Algorithm
    def quickSelect(l, r):
        # Pivot = rightmost value, pointer = leftmost part of the array
        pivot, pointer = nums[r], l
        for i in range(l, r):
            # Swapping the current value and the value at the pointer
            # if the current value is <= to the pivot
            if nums[i] <= pivot:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
        # Swapping the the pivot with the position of the pointer in the end
        nums[pointer], nums[r] = nums[r], nums[pointer]  # Pivot = nums[r]

        if pointer > kIndex: return quickSelect(l, pointer - 1)
        elif pointer < kIndex: return quickSelect(pointer + 1, r)
        else: return nums[pointer]
    return quickSelect(0, len(nums) - 1)

print(kthLargestElement(nums, k))
