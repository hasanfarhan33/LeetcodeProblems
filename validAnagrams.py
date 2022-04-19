#Valid anagram
s = "anagram"
t = "nagaram"

def validAnagram(s:str, t:str) -> bool:
    sortedStringS = sorted(s)
    sortedStringT = sorted(t)
    if sortedStringS == sortedStringT:
        return True
    else:
        return False

def validAnagramAnotherSolution(s:str, t:str)->bool: #NOT WOKRING
    hashsetS = set()
    hashsetT = set()
    if len(s) == len(t):
        for i in s:
            if i in hashsetS:
                continue
            else:
                hashsetS.add(i)
        for j in t:
            if j in hashsetT:
                continue
            else:
                hashsetT.add(j)
        if hashsetS == hashsetT:
            return True
        else:
            return False
    else:
        return False

# print(validAnagramAnotherSolution('ccac', 'aacc'))

def validAnagramNeetcode(s:str, t:str)->bool:
    if len(s)!=len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True

print(validAnagramNeetcode('star', 'rats'))




