# 23. Print sum of odd digits
n = 123456
total = 0
while n > 0:
    d = n % 10
    if d % 2 != 0:
        total += d
    n //= 10
print("sum of odd digits =", total)