n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
new_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        new_matrix[i][j] = matrix[n - 1 - j][i]

for row in new_matrix:
    print(*row)
