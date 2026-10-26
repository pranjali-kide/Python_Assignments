# 15. check whether number is divisible by both 3 and 7
num = int(input("enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Divisiable by both 3 and 7")
else:
    print("Not divisiable by 3 and 7")