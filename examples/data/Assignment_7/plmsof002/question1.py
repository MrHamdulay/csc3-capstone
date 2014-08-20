#Unique List
#Sofia Palmer
#29 April 2014


word = input("Enter strings (end with DONE):\n")
#make words into a list
words = []

#add each word to words list until DONE
while word != "DONE":
    unique = -1
    for i in range(len(words)):
        if (words[i] == word):
            unique = 0
    if unique == -1:
        words.append(word)
    word = input()
    
#iterate through the input words and check whether they are unique, if they are add them to the unique list
print()
print("Unique list:")
for i in range(len(words)):
    print(words[i])