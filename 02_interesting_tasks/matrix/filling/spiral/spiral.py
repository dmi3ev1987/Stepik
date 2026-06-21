n, m = [int(num) for num in input().split()]
matrix = [[0] * m for _ in range(n)]
counter = 1
start_r, end_r = 0, n - 1
start_c, end_c = 0, m - 1


while start_r <= end_r and start_c <= end_c:
    for j in range(start_c, end_c + 1):
        matrix[start_r][j] = counter
        counter += 1
    start_r += 1

    for i in range(start_r, end_r + 1):
        matrix[i][end_c] = counter
        counter += 1
    end_c -= 1

    if start_r <= end_r:
        for j in range(end_c, start_c - 1, -1):
            matrix[end_r][j] = counter
            counter += 1
        end_r -= 1

    if start_c <= end_c:
        for i in range(end_r, start_r - 1, -1):
            matrix[i][start_c] = counter
            counter += 1
        start_c += 1


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
