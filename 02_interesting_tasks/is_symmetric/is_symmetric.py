def is_symmetric(matrix, n):
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

print('YES' if is_symmetric(matrix, n) else 'NO')
