s = 'ABAB'
k = 2

def characterReplacement(s:str, k:int):
    count = {}
    left = 0
    res = 0
    maxFreq = 0
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)
        maxFreq = max(maxFreq, count[s[right]])

        while (right - left + 1) - maxFreq > k:
            count[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res


print(characterReplacement(s, k))

