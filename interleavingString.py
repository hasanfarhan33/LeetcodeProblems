'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

   * s = s1 + s2 + ... + sn
   * t = t1 + t2 + ... + tm
   * |n - m| <= 1
   * The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.
'''

from typing import List
from collections import defaultdict

s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'

def interleavingString(s1:str, s2:str, s3:str) -> bool:
    if len(s3) != len(s1) + len(s2): return False
    dp = [True for _ in range(len(s2) + 1)]
    for j in range(1, len(s2) + 1):
        dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
    for i in range(1, len(s1) + 1):
        dp[0] = (dp[0] and s1[i-1] == s3[i-1])
        for j in range(1, len(s2) + 1):
            dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
    return dp[-1]

print(interleavingString(s1, s2, s3))
