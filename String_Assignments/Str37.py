# 37. Find the longest word in a statement. 
s = input("Enter a sentence: ")
words = s.split()

if words:
    longest = max(words,key=len)
    print("Longest word:", longest)

else:
    print("No words found")