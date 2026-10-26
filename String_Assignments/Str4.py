# 4. Count the number of vowels in a string.
str = input("Enter a string: ")
count = 0

for ch in str.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)
