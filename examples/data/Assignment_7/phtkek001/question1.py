"""Kekolo Phetla
PHTKEK001
assignment 7 question 1"""





strings=input("Enter strings (end with DONE):\n")
stringlist=[]
while strings != "DONE":
    stringlist.append(strings)
    strings=input("")
    
    
print("")
print("Unique list:")
uniquelist=[]
for i in stringlist:
    if i not in uniquelist:
        uniquelist.append(i)
        print(i)
    else:
        if i in uniquelist:
            continue
  
        

            
            
