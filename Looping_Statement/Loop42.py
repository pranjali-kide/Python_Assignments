# 42. Calculate sum of square of first n numbers.
n = 5
total = 0
for i in range(1,n + 1):
    total += i ** 2
print("Sum of squares =", total)