print("Enter strings (end with DONE):")
x=input()
sList=[]
while x!="DONE":
        if x in sList:
                x=input("")
                continue
        else:
                sList.append(x)
                x=input("")
print("")
print("Unique list:")
for i in range(len(sList)):
        print(sList[i])
        

        