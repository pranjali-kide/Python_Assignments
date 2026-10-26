# 17. Find largest digit in a number.
n = 48259
largest = 0
while n > 0:
    d = n % 10
    if d > largest:
        largest = d
    n //= 10
print("Largest digit =", largest)