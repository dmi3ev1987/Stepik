def choose_plural(amount, declensions):
    number = amount % 100 if amount > 100 else amount
    number = number % 10 if number > 20 else number
    declension = ''
    if number == 1:
        declension = declensions[0]
    elif 2 <= number <= 4:
        declension = declensions[1]
    else:
        declension = declensions[2]
    return f'{amount} {declension}'

print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
