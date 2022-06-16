'''
Given a string s, return the longest palindromic substring in s.
'''

s = 'babad'

def longestPalindrome(s: str) -> str:
    res =""
    longestLen = 0
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if(r - l + 1) > longestLen:
                res = s[l:r+1]
                longestLen = r-l+1
            l-=1
            r+=1
        l, r = i, i+1
        while l>= 0 and r < len(s) and s[l] == s[r]:
            if(r-l+1) > longestLen:
                res = s[l:r+1]
                longestLen = r-l+1
            l-=1
            r+=1
    return res

print(longestPalindrome(s))

