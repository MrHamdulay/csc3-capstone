#Ashton Singh
#25 April 2014
#Lits


#Declaring list
words = []

#Getting string
word = input("Enter strings (end with DONE):\n")
while word.lower() != "done":
    words.append(word)
    word = input()

#Searching for longest word
longest = 0
for word in words:
    if len(word) > longest:
        longest = len(word)

#Inserting spaces in front of word in array for right alignment
print("\nRight-aligned list:")
for word in words:
    while len(word) < longest:
        word = " " + word
    print(word)