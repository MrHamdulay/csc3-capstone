#Done by Guy Green
#Unique words in a given list
#Assignment 7

GivenWords=[]
name=input("Enter strings (end with DONE):\n")
while name!="DONE":
    GivenWords.append(name)
    name=input("")

UniqueWords=[]
for i in range(len(GivenWords)):
    i=GivenWords[i]
    if i in UniqueWords:
        continue
    else:
        UniqueWords.append(i)

    
print("\nUnique list:")
for j in range(len(UniqueWords)):
    j=UniqueWords[j]
    print(j)