'''
Leetcode 2370: Longest Ideal Subsequence 
'''

from collections import defaultdict


s, k = "pvjcci", 2 

def longestIdealSubsequence(s: str, k: int) -> int:
    ascii_values = defaultdict() 
    num_to_return = 0 
    
    for c in range(len(s)): 
        ascii_values[c] = ord(s[c])
    
    for i in range(len(ascii_values) - 1): 
        abs_diff = abs(ascii_values[i] - ascii_values[i + 1])
        if abs_diff <= k: 
            num_to_return += 1 
            
    abs_diff = abs(ascii_values[len(ascii_values) - 2] - ascii_values[len(ascii_values) - 1])
    if abs_diff <= k: 
        num_to_return += 1
    return num_to_return

def longestIdealSubsequence_neet(s: str, k: int) -> int:
    
    cache = {}
    
    def helper(i, prev):
        if i == len(s): 
            return 0 
        
        res = helper(i + 1, prev)
        
        if prev == "" or abs(ord(s[i] - ord(prev))) <= k:
            res = max(res, 1 + helper(i + 1, s[i]))
            
        cache[(i, prev)] = res 
        return res 
    
def longestIdealSubstring_neet_two(s: str, k: int) -> int: 
    dp = [0] * 26 
    res = 0
    
    for c in s:
        curr = ord(c) - ord("a") # Creates a mapping from 0 - 25
        longest = 1 
        for prev in range(26):
            if abs(curr - prev) <= k:
                longest = max(longest, 1 + dp[prev])
        dp[curr] = max(dp[curr], longest)
    return max(dp)
                
print(longestIdealSubsequence(s, k))