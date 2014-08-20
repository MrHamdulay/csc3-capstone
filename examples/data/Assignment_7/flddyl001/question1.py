
myinput = input("Enter strings (end with DONE):\n")
mylist = []

while myinput != "DONE":
    
    if not myinput in mylist:
        mylist.append(myinput)
    myinput = input()
    
print("\nUnique list:")
for i in range(0,len(mylist)):
    
    print(mylist[i])
