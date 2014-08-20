#Amitha Doodnath
#DDNAMI001
#22/04/2014
#Programme to enter strings and format according to longest string

names=[]
nameLen=[]
count=0

a=input("Enter strings (end with DONE):\n")

while a != "DONE":
    names.append(a)
    nameLen.append(len(a))
    count+=1
    a=input()
    
print()    
print("Right-aligned list:")
if names:
    nameLen.sort()
    maxlen=str(nameLen[count-1])
    f="{0:>"+maxlen+"}"
    for i in range(count):
        r=f.format(names[i])
        print(r)