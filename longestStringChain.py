'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere
in wordA without changing the order of the other characters to make it equal to wordB.

    For example, "abc" is a predecessor of "abac", while "cba" is not a
    predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where
word1 is a predecessor of word2, word2 is a predecessor of word3, and so on.
A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given
list of words.
'''

from typing import List
from collections import defaultdict

words = ["a", "b", "ba", "bca", "bda", "bdca"]

def longestStrChain(words: List[str]) -> int:
    words.sort(key=len)
    res = 0
    dp = defaultdict(int)
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            predecessor = word[:i] + word[i+1:]
            if predecessor in dp and dp[word] < dp[predecessor] + 1:
                dp[word] = dp[predecessor] + 1
        res = max(res, dp[word])
    return res

print(longestStrChain(words))