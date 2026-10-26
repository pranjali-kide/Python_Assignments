# 39. Write a program to check whether a password is valid using nested if.
password = input("Enter password: ")

if len(password) >= 8:
    if password == "python123":
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("password must contain 8 characters")