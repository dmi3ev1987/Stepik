n, m = [int(num) for num in input().split()]
matrix = [[0] * m for _ in range(n)]
counter = 1

for k in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                matrix[i][j] = counter
                counter += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
