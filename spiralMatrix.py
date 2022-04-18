
def generateMatrix(n):
    spiralMatrix = [[]]
    if n == 0:
        return None
    if n == 1:
        spiralMatrix[0].append(n)
        return spiralMatrix
    if n > 1:
        numberToInsert = 1
        for numberToInsert in range(1, n+1):
            spiralMatrix[0].append(numberToInsert)

        return spiralMatrix

generateMatrixResult = generateMatrix(4)
print(generateMatrixResult)
