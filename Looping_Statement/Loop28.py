# 28. Check wether a number is Armstrong.
n = 153
original = n
digits = len(str(n))
total = 0
while n > 0:
    d = n % 10
    total += d ** digits
    n //= 10
print("Armstrong" if total == original else "Not Armstrong")