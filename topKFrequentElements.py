#TOP K FREQUENT ELEMTENTS
from typing import List

nums = [4, 1, -1, 2, -1, 2, 3]
k = 2

def topKFrequentElements(nums:List[int], k:int):
    if len(nums) != 0:
        numbersFrequency = {}
        frequentNumbers = []
        for i in nums:
            numbersFrequency[i] = numbersFrequency.get(i, 0) + 1
        print(numbersFrequency)
        # sortedNumbersFrequency = {k:v for k, v in sorted(numbersFrequency.items(), key = lambda item:item[1], reverse=True)}
        # keys = list(sortedNumbersFrequency.keys())
        for n, c in numbersFrequency.items():
            print(n, " : ", c)

def topKFrequentElementsNeetcode(nums:List[int], k:int):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append()
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


# topKFrequentElements(nums, k)