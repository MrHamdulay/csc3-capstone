"""print unique list of strings
Ross Eyre
27/04/2014"""

wordList = []
word = input("Enter strings (end with DONE):\n\n")

#get strings + populate list
while word != 'DONE':
    wordList.append(word)
    word = input()

#populate new unique word list
UniList = []
for i in wordList:
    if i not in UniList:
        UniList.append(i)

#print unique list    
print("Unique list:")
for wrd in UniList:
    print(wrd)