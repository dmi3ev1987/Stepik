n = int(input())
matrix = [['.'] * n for _ in range(n)]

for i in range(n):
    # для главной диагонали
    matrix[i][i] = '*'
    # для побочной диагонали
    matrix[i][n - 1 - i] = '*'
    # для средней строки
    matrix[n // 2][i] = '*'
    # для среднего столбца
    matrix[i][n // 2] = '*'

for row in matrix:
    print(*row)
