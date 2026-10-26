
# 22. Write a program to check salary bonus based on years of service.
Salary = float(input("Enter salary: "))
years = int(input("Enter years of service:"))

if years >= 5:
    bonus = Salary * 0.10
    print("Bonus =", bonus)
else:
    print("No bonus")