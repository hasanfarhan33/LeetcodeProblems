s = 'ABAB'
k = 2

def characterReplacement(s:str, k:int):
    count = {}
    i = 0
    res = 0
    for j in range(len(s)):
        count[s[j]] = 1 + count.get(s[j], 0)
        if (j-i+1) - max(count.values()) > k:
            count[s[i]] -= 1
            i += 1
        res = max(res, j - i + 1)
    return res


print(characterReplacement(s, k))

