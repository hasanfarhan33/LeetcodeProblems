from typing import List
'''
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal,
switching the matrix's row and column indices.
'''

matrix = [[1, 2, 3], [4, 5, 6]]

def transpose(matrix: List[List[int]]) -> List[List[int]]:
    rows = len(matrix)
    columns = len(matrix[0])

    newMatrix = [[0 for _ in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            newMatrix[j][i] = matrix[i][j]
    return newMatrix

print(transpose(matrix))