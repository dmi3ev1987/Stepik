n, m = [int(num) for num in input().split()]
matrix_a = [[int(num) for num in input().split()] for _ in range(n)]
input()
m, k = [int(num) for num in input().split()]
matrix_b = [[int(num) for num in input().split()] for _ in range(m)]
matrix_c = [[0] * k for _ in range(n)]


for i in range(n):
    for j in range(k):
        for q in range(m):
            matrix_c[i][j] += matrix_a[i][q] * matrix_b[q][j]

for i in range(n):
    for j in range(k):
        print(str(matrix_c[i][j]).ljust(3), end=' ')
    print()
