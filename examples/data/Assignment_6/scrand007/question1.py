string = input("Enter strings (end with DONE):\n")
list_1 = [string]
if string == "DONE":
    print()
    print("Right-aligned list:")
    pass
else:
    while string != "DONE":
        string = input()
        if string == "DONE":
            break
        else:
            list_1.append(string)
    
    max_length = len(max(list_1, key=len))    
    print()                                
    print("Right-aligned list:")
    t = 0
    for i in list_1:
        print(" "*(max_length-len(list_1[t])),list_1[t],sep='')
        t+=1
    