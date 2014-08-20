def namelist():
    names=[]
    maximum=0
    
    name=input("Enter strings (end with DONE):\n")
    if name=="DONE":
        pass
    else:
        names.append(name)
    
    while name != "DONE":
        name=input()
        if name=="DONE":
            continue
        else:
            names.append(name)
        
    for i in names:
        if len(i)>maximum:
            maximum=len(i)
    print()    
    print("Right-aligned list:")
    for j in names:
        x=(" "*(maximum-len(j)))
        print(x+j)
      
namelist()