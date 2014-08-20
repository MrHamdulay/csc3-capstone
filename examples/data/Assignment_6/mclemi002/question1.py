#emile mclennan
#assignment 6
#Q1


read=input("Enter strings (end with DONE):\n")
l=[]
while read!= "DONE":
    
    l.append(read)
    read=input("")
    

for i in range(len(l)):
    maxLength=len(l[0])
    if len(l[i]) > maxLength:
        maxLength= len(l[i])
    else: continue 

print()
print("Right-aligned list:")
    
for j in range(len(l)):
    print(l[j].rjust(maxLength))

    
    
