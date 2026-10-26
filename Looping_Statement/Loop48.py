# 48. Check whether number is strong number.
n = 145
original, total = n,0
while n > 0:
    d = n % 10
    fact = 1
    for i in range(1,d + 1):
        fact *= i
    total += fact
    n //= 10
print("Strong number"if total == original else "Not a strong number")