# 47. Find product of digits of a numbers.
n = 234
product = 1
while n > 0:
    product *= n % 10
    n //= 10
print("Product of digits =", product)