#kairav soni
print("Independent Electoral Commission")
print("--------------------------------")
names=input("Enter the names of parties (terminated by DONE):\n")
listnames=[]

while names!="DONE":
    listnames.append(names)
    names=input("")
listnames.sort()


i=0
length=(len(listnames)-1)
num=1
listvotes=[]


for j in range(length):
    
    
    if listnames[i]==listnames[i+1]:
        del listnames[i+1]
        num=num+1
        
        
    else:
        i=i+1
        listvotes.append(num)
        num=1
        
listvotes.append(num)



print("")
print("Vote counts:")
for i in range(len(listnames)):
    form="{0:" "<10}"
    print(form.format(listnames[i]), "-", listvotes[i])
