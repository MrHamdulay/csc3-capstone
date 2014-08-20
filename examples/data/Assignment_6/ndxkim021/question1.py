#kimberley naidoo
# 22 april 2014
#strings and lists


#list declaration
words = []

#Get string
word = input("Enter strings (end with DONE):\n")
while word.lower() != "done":
    words.append(word)
    word = input()

#search for longest word
longest = 0
for word in words:
    if len(word) > longest:
        longest = len(word)

#Insert spaces in front of word in array until total length equals the longest word
print("\nRight-aligned list:")
for word in words:
    while len(word) < longest:
        word = " " + word
    print(word)