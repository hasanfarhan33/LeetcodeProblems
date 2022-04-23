s = "abcabcbb"

def lenghtOfLongestSubstring(s):
    used = {}
    maxLength, start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c]+1
        else:
            maxLength = max(maxLength, i - start + 1)
        used[c] = i
    return maxLength


def lengthOfLongestSubstringNeetcode(s):
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

