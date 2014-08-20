"""Unique List Printer
Adam Edelberg
2014/04/29"""


word = input("Enter strings (end with DONE):\n")

wordList = []
printList = []


while (word != "DONE"):
    wordList.append(word)
    word = input()
    
    

for words in wordList:
    if words not in printList:
        printList.append(words)
    

print("\nUnique list:")
for i in printList:
    print(i)
