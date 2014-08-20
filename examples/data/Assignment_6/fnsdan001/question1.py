names = []
string = input("Enter strings (end with DONE):\n")
if string == "DONE":
    print()
    print("Right-aligned list:")
else:
    
    names.append(string)
    cnt = 1
    maxStr = string

    while string != "DONE":
        string = input("")
        if string!= "DONE":
            names.append(string)
            
            
    for i in names:
        if len(i)>len(maxStr):
            maxStr = i
    print()
    print("Right-aligned list:")
    

    for i in names:
        space = str(len(maxStr))
        print(('{:>' + space+ '}').format(i))
    
   


