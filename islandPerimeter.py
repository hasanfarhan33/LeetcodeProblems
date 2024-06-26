'''
Leetcode 463

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.

sample input = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

GRAPH PROBLEM! -> Solved using DFS or BFS 
'''

from typing import List

def islandPerimeter(grid: List[List[int]]) -> int: 
    visit = set() # To keep track of visited cell 
    
    def dfs(i, j): 
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0: 
            return 1
        if (i, j) in visit: 
            return 0 

        visit.add((i, j)
                  )
        perim = dfs(i, j + 1)
        perim += dfs(i + 1, j)
        perim += dfs(i, j - 1)
        perim += dfs(i-1, j)
        return perim 
    
    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            if grid[i][j]: 
                return dfs(i, j)
    

sample_input = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(islandPerimeter(sample_input))