# 25. Write a program to check type of triangle.
a = int(input("Enter first side"))
b = int(input("Enter Second side"))
c = int(input("Enter third side"))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")