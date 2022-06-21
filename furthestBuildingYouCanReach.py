'''
You are given an integer array heights representing the heights of buildings, some bricks, and
some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks
or ladders.

While moving from building i to building i+1 (0-indexed),

    If the current building's height is greater than or equal to the next building's height,
    you do not need a ladder or bricks.
    If the current building's height is less than the next building's height, you can either
    use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and
bricks optimally.
'''

from typing import List
import heapq

heights = [4, 2, 7, 6, 9, 14, 12]
bricks = 5
ladders = 1

def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    for i in range(len(heights) - 1):
        if i == len(heights) - 2 and heights[i] >= heights[i + 1]:
            return i + 1
        if heights[i + 1] > heights[i]:
            if (heights[i + 1] - heights[i]) <= bricks:  # Using bricks
                bricks = bricks - (heights[i + 1] - heights[i])
            elif (heights[i + 1] - heights[i]) > bricks and ladders != 0: # Using ladders
                ladders -= 1
            elif (heights[i + 1] - heights[i]) > bricks and ladders == 0: # Stuck
                return i
            elif bricks == 0 and ladders == 0 and heights[i + 1] > heights[i]: # Stuck
                return i


# USE PRIORITY QUEUES
def furthestBuildingPriorityQueue(heights: List[int], bricks:int, ladders:int) -> int:
    jumps_pq = []
    for i in range(len(heights) - 1):
        jumpHeight = heights[i + 1] - heights[i]
        if jumpHeight <= 0: continue
        heapq.heappush(jumps_pq, jumpHeight)
        if len(jumps_pq) > ladders:
            bricks -= heapq.heappop(jumps_pq)
        if bricks < 0: return i
    return len(heights) - 1

print(furthestBuildingPriorityQueue(heights, bricks, ladders))

# print(furthestBuilding(heights, bricks, ladders))
