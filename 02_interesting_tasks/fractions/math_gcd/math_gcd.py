from fractions import Fraction as F
from math import gcd

num = int(input())
numerator = num // 2
denominator = num - numerator

while gcd(numerator, denominator) != 1:
    numerator -= 1
    denominator += 1

print(F(numerator, denominator))
