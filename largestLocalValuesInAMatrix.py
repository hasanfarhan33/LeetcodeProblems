# LEETCODE 2373: Largest Local Values in A Matrix 

from typing import List


grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]

def largestLocal(grid: List[List[int]]) -> List[List[int]]: 
    # Creating an output matrix full of zeroes 
    outMat = [[0 for col in range(len(grid) - 2)] for row in range(len(grid) - 2)]
    outIndex = 0
    
    maxNum = float('-inf') 
    while outIndex < range(len(grid) - 2): 
        for i in range(3): 
            for j in range(3): 
                if grid[i][j] > maxNum: 
                    maxNum = grid[i][j] 
        outMat[outIndex][outIndex] = maxNum 
        outIndex += 1 
        maxNum = float('-inf')
        
        
def largestLocalNeet(grid: List[List[int]]) -> List[List[int]]: 
    # Four nested loop solution 
    N = len(grid)
    outMat = [[0] * (N - 2) for _ in range(N - 2)]
    
    for i in range(N - 2): 
        for j in range(N - 2): 
            for r in range(i, i + 3): 
                for c in range(j, j + 3): 
                    outMat[i][j] = max(outMat[i][j], grid[r][c])
    
    return outMat     
    
print(largestLocalNeet(grid))