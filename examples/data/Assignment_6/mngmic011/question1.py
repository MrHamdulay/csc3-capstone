"""question 1
assignment 6
Micaela Menegaldo"""

names=[]
name=""
max_string=0
print("Enter strings (end with DONE):")
while name!='DONE':
    names.append(name)
    name=input("")
    
for st in names:
    if len(st)>max_string:
        max_string=len(st)
del names[0]
print()
print("Right-aligned list:")
for i in names:
    print(" "*(max_string-len(i)),i,sep="")