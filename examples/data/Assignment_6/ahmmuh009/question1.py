def allign():
    longest=0
    list_1=[]
    string=input("Enter strings (end with DONE):\n")
    while string!="DONE":
        list_1.append(string)
        string=input("")
        if string=="DONE":
            break
    print("\nRight-aligned list:")
    longest=len(max(list_1, key=len))
    for i in list_1:
        if len(i)!=longest:
            print(" "*(longest-len(i))+i)
        elif len(i)==longest:
            print(i)
    
allign()
    