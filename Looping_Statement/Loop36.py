# 36. Find sum of numbers entered by user until () is enter.
total = 0
while True:
    num = int(input("Enter a number () to stop):"))
    if num == 0:
        break
    total += num
print("Sum =", total)