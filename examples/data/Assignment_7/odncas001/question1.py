"""word duplicate remover for given strings
casey o'donnell 
27 april 2014"""

print("Enter strings (end with DONE):")
newstring=[]
while True:
    inp=input("")
    if inp=="DONE":
        break
    if not inp in newstring:
        newstring.append(inp)
    else:
        continue
    
print()
print("Unique list:")
for i in newstring:
    print(i)
    
    