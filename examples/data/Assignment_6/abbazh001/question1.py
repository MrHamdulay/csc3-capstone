#Azhar Aboobaker
#ABBAZH001
#23/04/2014

def strings():
    x=[]
    y=input("Enter strings (end with DONE):\n")
    if y!="DONE":   
        x.append(y)
        while y:
            y=input()
            if y== "DONE":
                break        
            x.append(y)
    return x

def rightaligned():
    a=strings()
    if a!=[]:
        i=len(a[0])
        for j in a:
            if len(j)>=i:
                i=len(j)
        print()
        print("Right-aligned list:")
        for j in a:
            print(j.rjust(i))
    else:
        print()
        print("Right-aligned list:\n")

rightaligned()