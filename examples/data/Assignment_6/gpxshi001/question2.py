def main():
    
    VA= input("Enter vector A:\n")
    
    VB= input("Enter vector B:\n")
    
    
    VA= VA.split(" ") #turns vector inputs into a list
    VB= VB.split(" ")
    
    x1= eval(VA[0])
    x2= eval(VA[1])
    x3= eval(VA[2])
    y1= eval(VB[0])
    y2= eval(VB[1])
    y3= eval(VB[2])
    
    z= [x1+y1,x2+y2,x3+y3]
    
    dot= ((x1*y1)+(x2*y2)+(x3*y3))
    
    A= (((x1**2)+(x2**2)+(x3**2))**0.5)
    A="%0.2f" %(A)
    B= (((y1**2)+(y2**2)+(y3**2))**0.5)
    B="%0.2f" %(B)
    
    print("A+B =",z)
    print("A.B =",dot)
    print("|A| =",A)
    print("|B| =",B)

main()