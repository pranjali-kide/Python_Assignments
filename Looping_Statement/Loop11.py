#11. Count number of digit in a number.
n = 12345
n = abs(n)
count = 0
while n > 0:
    count += 1
    n //= 10
print("Digits =", count)