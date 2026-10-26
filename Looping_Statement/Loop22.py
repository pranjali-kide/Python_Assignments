# 22. find sum of even digits in a number.
n = 123456
total = 0
while n > 0:
    d = n % 10
    if d % 2 == 0:
        total += d
    n //= 10
print("Sum of even digirs =", total)