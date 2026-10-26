# 5. Count the number of consonants in a string.
str = input("Enter a string: ")
count = 0

for ch in str.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1

print("Consonants:",count)