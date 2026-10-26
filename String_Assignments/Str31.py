# 31. Remove punctuation marks from a string.
str = input("Enter a string: ")
result = ""

for ch in str:
    if ch not in str.punctuation:
        result += ch

print(result)