# 16. Write a program to find the greatest of three number.
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

if a >= b and a >= c:
    print("Greater =",a)
elif b >= a and b >= c:
    print("Greater =",b)
else:
    print("Greater =",c)