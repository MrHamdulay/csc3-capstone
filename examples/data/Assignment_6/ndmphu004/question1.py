#Phumelele Ndimande
#Assignment 6

list=[]
name= input("Enter strings (end with DONE):\n")
list.append(name)
while name != "DONE":
    name=input("")
    list.append(name) #add name to list
    
#find longest length    
max=len(list[0])
for names in list:
    if max<len(names):
        max=len(names)
    else:
        if max>len(names):
            max=max
print()
print("Right-aligned list:")  

for names in list:
    spaces=" " * (max-len(names)) #leaves space before names
    if names != "DONE":
        print(spaces+names)

