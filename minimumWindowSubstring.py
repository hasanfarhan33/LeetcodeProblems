'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
character in t (including duplicates) is included in the window. If there is no such substring, return the empty
string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
'''

from typing import List

s = "ADOBECODEBANC"
t = "ABC"

def minWindowSubstring(s:str, t:str) -> str:
    if t == "": return ""
    hashMapT, windowHash = {}, {}

    # Adding characters to hashmap t
    for c in t:
        hashMapT[c] = 1 + hashMapT.get(c, 0)

    have, need = 0, len(hashMapT)
    res, resLen = [-1, -1], float("infinity")
    left = 0

    for right in range(len(s)):
        c = s[right]
        windowHash[c] = 1 + windowHash.get(c, 0)
        if c in hashMapT and windowHash[c] == hashMapT[c]:
            have += 1

        while have == need:
            if (right - left + 1) < resLen:
                res = [left, right]
                resLen = (right - left + 1)
            windowHash[s[left]] -= 1
            if s[left] in hashMapT and windowHash[s[left]] < hashMapT[s[left]]:
                have -= 1
            left += 1
    left, right = res
    return s[left : right + 1] if resLen != float("infinity") else ""

print(minWindowSubstring(s, t))
