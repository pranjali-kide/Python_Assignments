# 7. Calculate factorial of a number using for loop.
n = 5
fact = 1
for i in range(1,n + 1):
    fact *= i
print(f"Factorial of {n} =", fact)