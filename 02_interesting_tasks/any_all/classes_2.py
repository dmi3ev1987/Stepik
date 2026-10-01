n = int(input())
classes = [[input().split() for _ in range(int(input()))] for _ in range(n)]
result = all(
    any(map(lambda student: int(student[1]) == 5, students)) for students in classes
)

print('YES' if result else 'NO')
