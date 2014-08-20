"""Right-align and print a list of given names
casey o'donnell
21 april 2014"""

names=[]

#collect names
print("Enter strings (end with DONE):")
while True:
    a=input("")
    if a=="DONE":
        break
    else:
        names.append(a)
        
#determine longest word
if names!=[]:
    longest=len(names[0])
    for i in names:
        if len(i) > longest:
            longest=len(i)
        
print()
print("Right-aligned list:")
for i in names:
    print(" "*(longest-len(i)), i,sep="")
    
    
    