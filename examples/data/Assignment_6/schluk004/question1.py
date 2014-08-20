name=""
namelist=[]
long=0

name=input("Enter strings (end with DONE):\n")

while(name!="DONE"):
    namelist.append(name)
    name=input()
    
for i in range(len(namelist)):
    if len(namelist[i])>long:
        long=len(namelist[i])

print("\nRight-aligned list:")
for i in range(len(namelist)):
    print((long-len(namelist[i]))*" ",namelist[i],sep="")