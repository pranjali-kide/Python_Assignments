# 32. Calculate power of a number without using pow().
base = 2
exp = 5
result = 1
for _ in range(exp):
    result *= base
print(f"{base}^{exp} =", result)