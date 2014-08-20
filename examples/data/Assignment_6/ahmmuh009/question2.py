import math
def vectors():
    a=[]
    b=[]
    first=input("Enter vector A:\n")
    second=input("Enter vector B:\n")
    vector_A=first.split(" ")
    vector_B=second.split(" ")
    for i in vector_A:
        a.append(int(i))
    for k in vector_B:
        b.append(int(k))
    no_1,no_2,no_3=float((a[0]*a[0])),float((a[1]*a[1])),float((a[2]*a[2]))
    no_4,no_5,no_6=float((b[0]*b[0])),float((b[1]*b[1])),float((b[2]*b[2]))
    print("A+B = [",a[0]+b[0],", ",a[1]+b[1],", ",a[2]+b[2],"]",sep="")
    print("A.B =",a[0]*b[0]+a[1]*b[1]+a[2]*b[2])
    x=round((math.sqrt(no_1+no_2+no_3)),2)
    y=round((math.sqrt(no_4+no_5+no_6)),2)
    if x==0.0 and y==0.0:
        print("|A| = 0.00")
        print("|B| = 0.00")
    else :
        print("|A| =",x)
        print("|B| =",y)        
        
vectors()
        