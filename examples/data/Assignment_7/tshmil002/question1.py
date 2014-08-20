#Mila Tshaka
#CSC1015F
#02 MAY 2014
uniqueList=[]
inpt=input("Enter strings (end with DONE):\n")
while inpt.lower()!="done":
    if inpt not in uniqueList:
        uniqueList.append(inpt)
    inpt=input()
print("\nUnique list:")
for i in uniqueList:
    print(i)