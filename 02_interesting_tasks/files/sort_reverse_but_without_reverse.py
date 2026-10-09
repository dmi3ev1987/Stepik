def count_bytes(filename):
    with open(filename) as file:
        data = file.read()
    new_line_count = data.count('\n')
    return filename, len(data) + new_line_count

result = [
    count_bytes(input())
    for _ in range(int(input()))
]

result.sort(key=lambda x: (-x[1], x[0]))
result = map(lambda x: f'{x[0]} {x[1]}B', result)

print(*result, sep='\n')                  
