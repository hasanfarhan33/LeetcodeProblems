'''
Given two strings s1 and s2, return true if s2 contains a
permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''

s1 = "ab"
s2 = "eidbaooo"

def checkInclusion(s1:str, s2:str) -> bool:
    s1Hash = {}
    windowHash = {}
    windowSize = len(s1)

    if windowSize > len(s2):
        return False

    for i in range(len(s1)):
        s1Hash[s1[i]] = 1 + s1Hash.get(s1[i], 0)

    comparePointer = 0
    endPointer = comparePointer + 1
    while (endPointer > comparePointer) and (endPointer < len(s2)):
        if s2[comparePointer] not in s1Hash:
            comparePointer += 1
            endPointer += 1
        else:
            print(s1Hash[s2[comparePointer]])
            break


    print(s1Hash)

def checkInclusionNeetcode()

checkInclusion(s1, s2)