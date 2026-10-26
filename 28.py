# 28. Write a program to calculate discounts based on total shopping amount.
amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

final_amount = amount-discount

print("Discount =", discount)
print("Final amount =",
final_amount)