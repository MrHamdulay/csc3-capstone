#2048 game functions
#1 may 2014
#kelly goosen

names = []
listofnames= input("Enter strings (end with DONE):\n")
while listofnames !='DONE':
    names.append(listofnames) #adding to empty list
    listofnames=input("")
    
nrrepeats=[]
for i in names:
    if i in nrrepeats:
        continue #continue if name is repeated
    else: #adds to list if it is not a repeat
        nrrepeats.append(i)
print()
print("Unique list:")
for x in nrrepeats:
    print(x)