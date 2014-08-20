slist= []
ulist= []
found=False

string=input("Enter strings (end with DONE):\n")
while(string!="DONE"):
    slist.append(string)
    string=input()
    
for i in slist:
    if i not in ulist:
        ulist.append(i)

print("\nUnique list:")        
for i in ulist:
    print(i)


    
