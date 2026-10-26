# 21. Write a program to find the smallest of three number.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a <= b and a <= c:
    print("Smallest no: ", a)
elif b <= a and b <= c:
    print("Smallest no: ", b)
else:
    print("smallest no: ", c)