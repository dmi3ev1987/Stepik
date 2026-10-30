def get_biggest(numbers):
    if not numbers:
        return -1
    numbers = [str(num) for num in numbers]
    length = len(numbers)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if numbers[j] + numbers[min_index] > numbers[min_index] + numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return int(''.join(numbers))

print(get_biggest([1, 2, 3]))
print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))
print(get_biggest([]))
print(get_biggest([0, 0, 0, 0, 0, 0]))
print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))
print(get_biggest([7, 7, 7, 7, 7, 7, 7, 7, 7]))
print(get_biggest([62, 626]))
