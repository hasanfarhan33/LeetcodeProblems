'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the
following properties:

   * Integers in each row are sorted from left to right.
   * The first integer of each row is greater than the last integer of the previous row.
'''

from typing import List

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    for j in range(ROWS):
        if matrix[j][0] < target and matrix[j][-1] > target:
            left, right = 0, COLS - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[j][mid] > target:
                    right = mid - 1
                elif matrix[j][mid] < target:
                    left = mid + 1
                else: return True
    return False

searchMatrix(matrix, target)