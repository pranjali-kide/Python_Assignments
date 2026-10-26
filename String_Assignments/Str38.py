# 38. Find the shortest word in a sentence.
s = input("Enter a sentence: ")
words = s.split()

if words:
    shortest = min(words, key=len)
    print("Shortest word:",shortest)
else:
    print("No words found")