listA=[]
x=input("Enter strings (end with DONE):\n")
while x!="DONE":
    listA.append(x)
    x=input("")

long=0
for i in listA:
    if len(i)>long:
        long=len(i)
print()
print("Right-aligned list:")
for a in listA:
        new=" "*(long-len(a))+a
        print(new)

    
    
    
    
    
    
    
    
    
    