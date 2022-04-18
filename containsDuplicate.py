nums = [1, 4, 3, 2, 1, 4]

def containsDuplicate(nums):
    visitedMap = set()
    if not nums or len(nums) == 1:
        return False
    elif len(nums) == 2:
        if nums[0] == nums[-1]:
            return True
        else:
            return False
    else:
        for i in range(len(nums)):
            if nums[i] in visitedMap:
                return True
            else:
                visitedMap.add(nums[i])
        return False


containsDuplicate(nums)

