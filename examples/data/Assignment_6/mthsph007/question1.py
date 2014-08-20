"""Sphiwe Muthembi
   Mthsph007
   Assignment 6 - Question 1
   Lists/ Arrays"""

name= input("Enter strings (end with DONE):\n")

if name == "DONE":
    print()
    print('Right-aligned list:')
else:
    
    arnames= []
    arnames.append(name)

    while name != "DONE":
        name= input()
        arnames.append(name)
        

    
    arnames.remove("DONE") # Remove DONE from array because the sentinal loop will automatically append it to the end of the array.
    print()
    print("Right-aligned list:")
    x=arnames[0]
    for i in range(len(arnames)):
                       
        if len(x) < len(arnames[i]):
                            
            x= arnames[i]
    for k in range(len(arnames)):
            
        space = len(x) - len(arnames[k])
        print(" "*space+arnames[k])
            

    
   # y="{0:>10}".format(x)
   # print(y)
    
    
    
    