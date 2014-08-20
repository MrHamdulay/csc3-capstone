#right align list of names

#get a list of names
names=[]
name=input("Enter strings (end with DONE): \n")
while name!="DONE":
    names.append(name)
    name=input("")

#right align list of names
print("")
print("Right-aligned list:")
for i in names:
    n=len(max(names, key=len))   #determine length of longest name
    gap=n-len(i)                 #spaces to align
    print(gap*" ", i, sep="")     