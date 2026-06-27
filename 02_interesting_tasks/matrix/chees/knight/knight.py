horse = input()
row, col = '87654321'.index(horse[-1]), 'abcdefgh'.index(horse[0])
n = 8
board = [['.'] * n for _ in range(n)]
board[row][col] = 'N'
moves = [
    [row + 2, col + 1],
    [row + 2, col - 1],
    [row - 2, col + 1],
    [row - 2, col - 1],
    [row + 1, col + 2],
    [row + 1, col - 2],
    [row - 1, col + 2],
    [row - 1, col - 2],
]

for move in moves:
    if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
        board[move[0]][move[1]] = '*'

for row in board:
    print(*row)
