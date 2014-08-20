x=""
list=[] #create empty list
print("Enter strings (end with DONE):")
while x != "DONE":
    x=input()
    if x!= "DONE": #specify when adding ends
        list.append(x)
print("") #skip line
max=0
for i in range(len(list)):
    if len(list[i])>max:
        max=len(list[i]) #find max
print("Right-aligned list:")
for j in range(len(list)):
    space=max-len(list[j]) #amount of spaces before
    print(space*" ", list[j], sep="") 

        
