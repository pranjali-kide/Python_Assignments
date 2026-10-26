#29. Write a program to check blood donation eligiblity based on age and weight.
age = int(input("Enter a age"))
weight = int(input("Enter a weight"))

if age >= 18 and weight >= 40:
    print("eligible for blood donation")
else:
    print("Not eligible for blood donation")