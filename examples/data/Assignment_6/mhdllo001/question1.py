list=[]
name=""
print("Enter strings (end with DONE):")

while(name!="DONE"):
    
    name=input()

    list.append(name)
    
    
list.remove("DONE")
longest=1   
for i in list:
    if(longest<len(i)):
        longest=len(i)


print()
print("Right-aligned list:")
for i in list:
    print(" "*(longest-len(i)),i,sep='')