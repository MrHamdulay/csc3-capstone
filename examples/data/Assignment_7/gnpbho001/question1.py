#GNPBHO001
#Akshay.G




names=[]
name=input("Enter strings (end with DONE):\n")
while name!="DONE":
    names.append(name)
    name=input()
    
    
strings=[]
for i in names:
    if i not in strings:
        strings.append(i)
    else:
        pass

print("\nUnique list:")  
for i in strings:
    print(i)
    
    


