numbers_1, numbers_2 = set(input().split()), set(input().split())

print(*sorted(numbers_1 & numbers_2, key=int))
