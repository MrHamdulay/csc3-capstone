'''Program to take a list of strings and print the in the same order but without duplicates
By Daniel Newton
27/04/14'''

StrList=[]
print("Enter strings (end with DONE):")

DONE=True
while DONE == True:     #asks for user input until "DONE" is typed
    word=input()
    if word=="DONE":
        break
    else:
        StrList.append(word)

PrintList=[]
for i in StrList:       #adds elements of first list to new list, but does not allow duplications, and checks through new list previously to scan for existing equal element.
    if i in PrintList:
        continue
    else:
        PrintList.append(i)

print("\nUnique list:")     #prints the new list line by line
for i in PrintList:
    print(i)