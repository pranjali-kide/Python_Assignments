# 37. Print numbers until user enters a negative numbers.
while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    print(num)