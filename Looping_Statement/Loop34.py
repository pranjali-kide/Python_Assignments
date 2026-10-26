# 34. Check whether a string is palindrome.
s = "madam"
rev = ""
for ch in s:
    rev = ch + rev
print("Palindrome" if s == rev else "Not a palindrome")