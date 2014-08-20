
uniqueList= []

x=input("Enter strings (end with DONE):\n")

if x!="DONE":
    uniqueList.append(x) 

    while (x!="DONE"):

        x=input()
        if x in uniqueList:
            pass
        elif x=="DONE":
            pass
        else:
            uniqueList.append(x)

    print()
    print("Unique list:")

    for i in uniqueList:
      print(i)


else:
    
    print()
    print("Unique list:")
       



 
