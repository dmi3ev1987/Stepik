n, m = [int(num) for num in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1

for row in matrix:
    for num in row:
        print(str(num).ljust(3), end=' ')
    print()
