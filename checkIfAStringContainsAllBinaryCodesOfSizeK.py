'''Given a binary string s and an integer k, return true if every binary code of
length k is a substring of s. Otherwise, return false.'''

s, k = "00110110", 2

def hasAllCodes(s:str, k:int) -> bool:
    codeSet = set()
    for i in range(len(s) - k + 1):
        codeSet.add(s[i: i+k])
    return len(codeSet) == 2**k

print(hasAllCodes(s, k))