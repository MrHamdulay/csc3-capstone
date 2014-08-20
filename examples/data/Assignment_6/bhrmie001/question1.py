def strings():
    y=[]
    x=input("Enter strings (end with DONE):\n")
    if x!="DONE":   
        y.append(x)
        while x:
            x=input()
            if x== "DONE":
                break        
            y.append(x)
    return y

def aligned():
    z=strings()
    if z!=[]:
        j=len(z[0])
        for i in z:
            if len(i)>=j:
                j=len(i)
        print()
        print("Right-aligned list:")
        for i in z:
            print(i.rjust(j))
    else:
        print()
        print("Right-aligned list:\n")

aligned()