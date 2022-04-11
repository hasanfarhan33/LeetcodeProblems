grid = [[2,5,8,5], [1,5,5,2], [9,1,3,9], [4,2,6,7]]

def shiftGrid(grid, k):
    m, n = len(grid), len(grid[0])
    start = m * n - k % (m * n)
    ans = []
    for i in range(start, m * n + start):
        j = i % (m * n)
        r, c = j // n, j % n
        if not (j - start) % n:
            ans.append([])
        ans[-1].append(grid[r][c])
    return ans

print(grid)
print("Shifted grid: ", shiftGrid(grid, 3))