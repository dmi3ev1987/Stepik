def pascal(n):
    result = []
    cur_row = [1]
    for _ in range(n):
        result.append(cur_row)
        cur_row = [0] + cur_row + [0]
        new_row = [
            cur_row[i] + cur_row[i + 1] for i in range(len(cur_row) - 1)
        ]
        cur_row = new_row
    return result


n = int(input())
for row in pascal(n):
    print(*row)
