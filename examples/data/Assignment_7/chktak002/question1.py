x=input("Enter strings (end with DONE):\n")
unique=[]

while x !="DONE":
    if x not in unique:
        unique.append(x)
        x=input()
    else:
        x=input()


print()
print("Unique list:")
for i in range(len(unique)):
    print(unique[i], end='\n')
    
    
    

