board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]

board1 = [[0],
          [1],
          [1]]

print("Number of rows: ", len(board))
print("Number of column: ", len(board[0]))

def gameOfLife(board):

    # IF THERE IS ONLY ONE COLUMN
    if len(board[0]) == 1:
        for j in range(len(board)):
            # AT THE TOP OF THE BOARD
            if (j == 0 and board[0][j] == 0) or (j == len(board) - 1 and board[0][j]==0):
                board[0][j] = 0
            elif (j == 0 and board[0][j] == 1) or (j == len(board) - 1 and board[0][j]==1):
                board[0][j] = 0
            # MIDDLE OF THE BOARD
            if j > 0:
                if board[0][j] == 0:
                    board[0][j] = 0
                if board[0][j] == 1:
                    if board[0][j - 1] == 0 or board[0][j + 1] == 0:
                        board[0][j] = 0
                    else:
                        board[0][j] = 1




def gameofLifeNeetCode(board):
    ROWS, COLS = len(board), len(board[0])
    def countNeighbors(r, c):
        nei = 0
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if ((i == r and j == c) or i < 0 or j < 0 or i == ROWS or
                        j == COLS):
                    continue
                if board[i][j] in [1, 3]:
                    nei += 1
        return nei


    for r in range(ROWS):
        for c in range(COLS):
            nei = countNeighbors(r, c)
            if board[r][c]:
                if nei in [2, 3]:
                    board[r][c] = 3
                elif nei == 3:
                    board[r][c] = 2

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                board[r][c] = 0
            elif board[r][c] in [2, 3]:
                board[r][c] = 1