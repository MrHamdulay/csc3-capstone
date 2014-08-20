"""this program removes any duplicated string within a list while still keeping the orignal order
quincy cele
27 april 2014"""
#convert the input into a list and continuously add more strings into the list until the word "done" has been supplied. create an additional empty list.
strings=input("Enter strings (end with DONE):\n")
listed=[]
par=[]
if strings!="DONE":
    listed.append(strings)

while strings!="DONE":
    
    strings=input()
    if strings!="DONE":
        listed.append(strings)
#only add the one of any duplicate words into the additional list
for i in listed:
    if i not in par:
        par.append(i)
print()
print("Unique list:")
for i in par:
    print(i)