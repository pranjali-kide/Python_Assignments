# 32. Write a program to check whether a person can apply for a loan.
age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))

if age >= 21:
    if salary >= 25000:
        print("Eligible for loan")
    else:
        print("Not eligible due to low salary")
else:
    print("Not eligible due to age")