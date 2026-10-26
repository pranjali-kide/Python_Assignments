#20.  Write a program to check tickit price based on age.
age = int(input("Enter a age"))

if age < 5:
    print("Tickit is free")
elif age < 18:
    print("Ticket price = Rs. 50")
elif age < 60:
    print("Ticket price = Rs. 100")
else:
    print("Ticket price = Rs. 70")