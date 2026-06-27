queen = input()  # c4
row, col = '87654321'.index(queen[-1]), 'abcdefgh'.index(queen[0])
n = 8
board = [['.'] * n for _ in range(n)]


for i in range(n):
    board[row][i] = '*'
    board[i][col] = '*'
    for j in range(n):
        if abs(row - i) == abs(col - j):
            board[i][j] = '*'

board[row][col] = 'Q'

for row in board:
    print(*row)
