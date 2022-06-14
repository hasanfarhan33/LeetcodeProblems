'''
Given two strings word1 and word2, return the minimum number of steps required to
 make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
'''

word1 = "ate"
word2 = "eat"

def minDistance(word1: str, word2: str) -> int:
    if word1 == word2:
        return 0
    res = 0

    word1Array = [0] * 26
    word2Array = [0] * 26

    for i, n in enumerate(word1):
        word1Array[ord(n) - ord('a')] += 1
    for i, n in enumerate(word2):
        word2Array[ord(n) - ord('a')] += 1

    for i in range(len(word2Array)):
        if word1Array[i] == word2Array[i]:
            continue
        else:
            res += abs(word2Array[i] - word1Array[i])


    print(word1Array)
    print(word2Array)
    return res

def dpMinDistance(word1:str, word2:str) -> int:
    N, M = len(word1), len(word2)
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

    for c in range(N + 1):
        dp[0][c] = c
    for r in range(M + 1):
        dp[r][0] = r

    for r in range(1, M + 1):
        for c in range(1, N + 1):
            if word1[c-1]==word2[r-1]:
                dp[r][c] = dp[r-1][c-1]
            else:
                dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1])
    print(dp)
    return dp[-1][-1]


# print(minDistance(word1, word2))
print(dpMinDistance(word1, word2))