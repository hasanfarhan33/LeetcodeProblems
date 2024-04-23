'''
Given two strings s1 and s2, return true if s2 contains a
permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''

from typing import Counter


s1 = "abc"
s2 = "bbbca"

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

def checkInclusionNeetcode(s1: str, s2:str) -> bool:
    if len(s1) > len(s2): return False
    s1Count, s2Count = [0] * 26, [0] * 26

    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0 )

    left = 0
    # Starting from the next character after creating the hash arrays (s1Count, s2Count)
    for right in range(len(s1), len(s2)):
        if matches == 26: return True

        # Adding the rightmost letter in the array
        index = ord(s2[right]) - ord('a')
        s2Count[index] += 1
        if s2Count[index] == s1Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        # Removing the leftmost letter in the array
        index = ord(s2[left]) - ord('a')
        s2Count[index] -=1
        if s2Count[index] == s1Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        left +=1
    return matches == 26

def checkInclusionHashMap(s1: str, s2: str) -> bool: 
        s1_map = Counter(s1)
        s2_map = Counter()

        if len(s1) > len(s2):
            return False

        for i in range(len(s2)):
            s2_map[s2[i]] += 1
            if i >= len(s1):
                if s2_map[s2[i - len(s1)]] > 1:
                    s2_map[s2[i - len(s1)]] -= 1                    
                else:
                    del s2_map[s2[i - len(s1)]]
            if s1_map == s2_map:
                return True 

        return False


        

# checkInclusion(s1, s2)
print(checkInclusionHashMap(s1, s2))