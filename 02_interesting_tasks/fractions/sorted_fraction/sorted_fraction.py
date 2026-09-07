from fractions import Fraction as F
from math import gcd


n = int(input())
result = []

# Перебираем все возможные знаменатели от 2 до n
for denominator in range(2, n + 1):
    # Перебираем все числители от 1 до denominator-1 (дроби между 0 и 1)
    for numerator in range(1, denominator):
        # Проверяем, что дробь несократимая (НОД числителя и знаменателя = 1)
        if gcd(numerator, denominator) == 1:
            result.append(F(numerator, denominator))

result.sort()
print(*result, sep='\n')
