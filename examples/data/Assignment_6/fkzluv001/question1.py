"""Luvo Fokazi
22/04/2014"""
stringList=[] #initialises list to store strings
longest=0
i=0
#prompt input of strings from user
name=input("Enter strings (end with DONE):\n")
while name!="done" and name!="DONE":
    stringList.append(name) #populates array of strings
    i+=1
    if longest<len(name):
        longest=len(name)
    name=input()
formater="{0:>"+str(longest)+"}"
print("\nRight-aligned list:")
for j in stringList:
    print(formater.format(j))