"""A program that takes a list of names and prints them right aligned
Jason Findlay
23/04/2014"""

Name=input("Enter strings (end with DONE):\n")
names=[]
Count=0
length=0

#fill list
while Name!="DONE":
    if Name=="DONE":
        break
    else:
        names.append(Name)
    Name=input()

#find longest string
for i in range(len(names)):
    if len(names[i])>length:
        length=len(names[i])

#print list of names
print()
print("Right-aligned list:")

for i in range(len(names)):
    print(names[i].rjust(length))
    

