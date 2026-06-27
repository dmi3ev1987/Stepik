def is_symmetric(matrix, n):
    for i in range(n):
        for j in range(n - i - 1):
            if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
                return 'NO'
    return 'YES'


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

print(is_symmetric(matrix, n))
