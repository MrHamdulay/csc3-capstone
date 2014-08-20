def Duplicate():
    print("Enter strings (end with DONE):")
    print()
    line=[]
    unique=[]
    ip=input()
    while ip!="DONE":
        line.append(ip)
        if ip not in unique:
            unique.append(ip)
            
        ip=input()
        if ip=="DONE":
            break
    print("Unique list:")
    for uni in unique:
        print(uni)
               
Duplicate()