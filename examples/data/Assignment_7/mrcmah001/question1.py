x=""
list1=[]
list2=[]  #empty lists
print("Enter strings (end with DONE):")
print("")
while x != "DONE": #specify when adding ends
    x=input()
    if x!= "DONE":
        list1.append(x)
for i in list1:
    if i not in list2:
        list2.append(i) #create unique list
print("Unique list:")
for j in list2:
    print(j)  #print unique list