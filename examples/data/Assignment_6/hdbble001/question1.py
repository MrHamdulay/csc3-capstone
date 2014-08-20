string=input("Enter strings (end with DONE):\n")

list=[]

while not string=='DONE':
    list.append(string)
    string=input()
    if string=="DONE":
        break
    

fieldW=0
for i in list:
    wrdLength=len(i)
    if wrdLength > fieldW:
        fieldW=wrdLength
print()
print("Right-aligned list:")
for i in list:
    print(" "*(fieldW-(len(i))), i, sep="")
    
