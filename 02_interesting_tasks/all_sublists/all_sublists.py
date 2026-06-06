symbols = input().split()
n = len(symbols)
result = [[]]

for i in range(1, n):
    for j in range(n):
        sub_list = symbols[j : j + i]
        if len(sub_list) == i:
            result.append(sub_list)

result.append(symbols)
print(result)
