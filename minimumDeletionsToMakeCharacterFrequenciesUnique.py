'''
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab",
the frequency of 'a' is 2, while the frequency of 'b' is 1.
'''

from typing import List
from collections import Counter

s = 'ceabaacb'

def minDeletions(s: str) -> int:
    count, res, seen = Counter(s), 0, set()
    for c, frequency in count.items():
        while frequency > 0 and frequency in seen:
            frequency -= 1
            res += 1
        seen.add(frequency)
    return res

print(minDeletions(s))