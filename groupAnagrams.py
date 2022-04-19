from typing import List
from collections import defaultdict

strs = ["car", "eat", "ate", "tea", "tan", "nat", "bat", "rat"]

def groupAnagrams(str:List[str]) -> List[List[str]]:
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26 #a - z
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()

print(groupAnagrams(strs))