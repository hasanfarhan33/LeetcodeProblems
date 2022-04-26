from typing import List

points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

def minCostConnectPoints(points: List[List[int]]):
    n = len(points)
    parents = list(range(n))

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        r1 = find(x)
        r2 = find(y)

        if r1 != r2:
            parents[r2] = r1
            return True
        else:
            return False

    def getDist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    paths = []
    for i in range(n):
        for j in range(i+1, n):
            dist = getDist(points[i], points[j])
            paths.append((dist, i, j))
    paths.sort()
    res = 0
    for dist, p1, p2 in paths:
        if union(p1, p2):
            res+=dist
    return res




minCostConnectPoints(points)