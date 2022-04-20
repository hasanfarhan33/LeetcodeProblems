arr = [39, 4, 23, 12, 49, 38, 39, 10]
nums = sorted(arr)

def removeDuplicates(nums)->int:
    x = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[x] = nums[r]
            x+=1
    return x

removeDuplicates(nums)
