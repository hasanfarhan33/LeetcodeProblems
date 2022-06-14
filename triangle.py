'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move to either
 index i or index i + 1 on the next row.
'''

from typing import List

triangle = [[2], [3, 4], [6, 5, 4], [4, 1, 8, 3]]

def minimumTotal(triangle: List[List[int]]) -> int:
    ROWS = len(triangle)
    COLS = len(triangle[0])
    minTotal = i = j = 0

    if ROWS == 1:
        return triangle[0][0]

    while j < ROWS:
        if j == 0:
            minTotal += triangle[j][i]
            j += 1
        if triangle[j][i] <= triangle[j][i+1]:
            minTotal += triangle[j][i]
            j += 1
        else:
            minTotal += triangle[j][i+1]
            j += 1
    return minTotal

def minimumTotalNeetcode(triangle: List[List[int]]) -> int:
    dp = [0] * (len(triangle) + 1)
    for row in triangle[::-1]:
        for i, n in enumerate(row):
            dp[i] = n + min(dp[i], dp[i + 1])
    return dp[0]

print(minimumTotalNeetcode(triangle))