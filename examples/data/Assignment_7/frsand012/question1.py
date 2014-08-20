def unique():
    
    names=[]
    
    name=input("Enter strings (end with DONE):\n")
    while name != "DONE":
        names.append(name)
        name=input("")
    
    arrange=[]
    for name in names:
        if name not in arrange:
            arrange.append(name)
    
    print()
    print("Unique list:")
    for i in arrange:
        print(i)
    
unique()