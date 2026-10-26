# 15. Sum of digits
n = 1234
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits =", total)