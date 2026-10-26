# 33. Write a program to check lone year and century year.
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap year and century year")
elif year % 100 == 0:
    print("Century year but not leap year")
elif year % 4 == 0:
    print("Leap year but not century year")
else:
    print("Not a leap year")