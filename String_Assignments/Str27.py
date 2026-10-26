# 27. Check whether a word exists in a sentence.
s = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in s.split():
    print("Word exists")
else:
    print("word does not exist")