# 13. check the palindrome number.
n = 121
original,rev = n,0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("palindrome" if original == rev else "Not a palindrome")