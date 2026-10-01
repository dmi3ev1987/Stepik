n = int(input())

for _ in range(n):
    k = int(input())
    students = [input().split() for _ in range(k)]
    result = any(map(lambda student: int(student[1]) == 5, students))
    if not result:
        print('NO')
        break
else:
    print('YES')
