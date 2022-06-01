from typing import List

'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

strs = ["flower", "flow", "flight"]

def longestCommonPrefix(strs: List[str]) -> str:
    numWords = len(strs)
    res = ""
    ptr1 = 0
    ptr2 = 1
    cIndex = 0
    if numWords == 1 or len(strs[0]) == 0:
        return ""
    # print(strs[ptr2][cIndex])
    while True:
        if cIndex <= len(strs[ptr1]) and cIndex <= len(strs[ptr2]):
            if strs[ptr1][cIndex] == strs[ptr2][cIndex]:
                ptr2+=1
            else:
                return res
            if ptr2 == numWords:
                res += strs[ptr1][cIndex]
                ptr2 = 1
                cIndex += 1
        else:
            return res
    return res

def neetcodeLongestCommonPrefix(strs: List[str]) -> str:
    res = ""
    for i in range(len(strs[0])):
        for string in strs:
            if i == len(string) or string[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res

neetcodeLongestCommonPrefix(strs)