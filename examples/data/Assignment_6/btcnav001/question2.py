
def main():
    x=input("Enter vector A:\n")
    y=input("Enter vector B:\n")
    x=x.split(" ")
    y=y.split(" ")
    x1=eval(x[0])
    x2=eval(x[1])
    x3=eval(x[2])
    y1=eval(y[0])
    y2=eval(y[1])
    y3=eval(y[2])

    z=[x1+y1,x2+y2,x3+y3]
    
    dot=((x1*y1)+(x2*y2)+(x3*y3))

    A=(((x1**2)+(x2**2)+(x3**2))**0.5)
    A="%0.2f" % (A)
    B=(((y1**2)+(y2**2)+(y3**2))**0.5)
    B="%0.2f" % (B)
    print("A+B =",z)
    print("A.B =",dot)
    print("|A| =",A)
    print("|B| =",B)
    
main()