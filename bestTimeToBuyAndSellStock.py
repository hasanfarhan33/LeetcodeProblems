from typing import List

useCases = [[7,1,5,3,6,4], [7,6,4,3,1], [1,2], [1,2,4], [2,1,2,1,0,1,2]]

def maxProfit(prices:List[int]) -> int:
    i = 0
    j = i + 1
    maxDifference = 0
    while i < j and ((j < len(prices)) and (i < len(prices) - 1)):
        difference = prices[j] - prices[i]
        if difference < 0:
            i += 1
            j += 1
        else:
            j += 1
            if difference > maxDifference:
                maxDifference = difference
    return maxDifference

for useCase in useCases:
    print(maxProfit(useCase))

