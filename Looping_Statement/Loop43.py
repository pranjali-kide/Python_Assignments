# 43. Calculate Sum of cubes of first n number.
n = 5
total = 0
for i in range(1,n + 1):
    total += i ** 3
print("Sum of cubes =", total)