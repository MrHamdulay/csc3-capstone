print("Enter strings (end with DONE):")
listed=[]
c=input()
while c!="DONE":
    listed.append(c)
    c=input()
    
x=0    
for c in listed:
    if len(c)>x:
        x=len(c)
    else:
        continue
    
print()    
print("Right-aligned list:")
for c in listed:
    print(" "*(x-len(c)),c,sep="")