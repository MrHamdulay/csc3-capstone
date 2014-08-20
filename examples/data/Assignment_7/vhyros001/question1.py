"""Assignment 7 question 1 remove duplicates from list
Ross van der Heyde VHYROS001
29 April 2014"""

def removeDup(l):
    """Remove duplicates from list, store in new list"""
    newList =[]
    for i in l:
        if i not in newList:
            newList.append(i)
    return newList

words = [] # list to store word entered by user
word = input("Enter strings (end with DONE):\n")
while word != "DONE":
    words.append(word) #add words entered to list
    word = input()    
    
# call function to remove duplicates
newList = removeDup(words)

#print list with unique words
print("\nUnique list:")
for i in newList :
    print(i)
