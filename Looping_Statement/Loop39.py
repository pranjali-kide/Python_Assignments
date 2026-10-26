# 39. Count total words in a string.
s = "Pyhton loop are easy to learn"
count = 0
in_word = False
for ch in s:
    if ch != " " and not in_word:
        count = 1
        in_word = True
    elif ch == " ":
        in_word = False
print("Words = ", count)