# LEETCODE 26: Removing Duplicated from sorted array 

nums = [0,0,1,1,1,2,2,3,3,4]


def removeDuplicates(nums)->int:
    leftPointer = 1 
    
    for rightPointer in range(1, len(nums)): 
        if nums[rightPointer] != nums[rightPointer - 1]: 
            nums[leftPointer] = nums[rightPointer]
            leftPointer += 1 
    
    return leftPointer 

removeDuplicates(nums)
