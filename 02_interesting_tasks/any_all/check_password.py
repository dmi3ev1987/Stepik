def check_password(s):
    lower = any(char.islower() for char in s)
    upper = any(char.isupper() for char in s)
    digit = any(char.isdigit() for char in s)
    return lower, upper, digit


s = input()

if len(s) >= 7 and all(check_password(s)):
    print('YES')
else:
    print('NO')
