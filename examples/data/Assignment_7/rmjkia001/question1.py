"""Delete Duplicate
Kiara Ramjith
April 2014"""
dupList=[] # declare a new array
word=input("Enter strings (end with DONE):\n")
while word!= "DONE": #fill the array
    dupList.append(word)
    word=input("")
unList=[] # declare a new array
for i in range (len(dupList)):
    if dupList[i] not in unList: # if the current word of the old array doesn't exist in the old one, put it in the new one
        unList.append(dupList[i])
print("\nUnique list:") #print new array
for i in range (len(unList)):
    print(unList[i])

    
    