"""This program performs the basic vector calculations in 3 dimensions: addition, dot product and normalization
Hebert Tema
21-04-2014"""

#prompt the user for input
A=input("Enter vector A:\n")
B=input("Enter vector B:\n")


def vector_calculations(A,B):
    import math
    
    list_A=A.split()                               #split the entered strings
    list_B=B.split()
    
    length=len(list_A)
    
    addition=[]                                   #initialise the variables
    product=0
    squareA=0
    squareB=0
    
    for i in range(length):
        a=eval(list_A[i])
        b=eval(list_B[i])
        
        addition.append(a+b)
       
        product+=(a*b)
       
        squareA+=a**2
        squareB+=b**2
    
    #print out the output
    print("A+B =",addition)                       #addition
    print("A.B =",round(product, 2))              #dot product
    print("|A| =","{0:0<4}".format(round(math.sqrt(squareA), 2)))   #normalization
    print("|B| =","{0:0<4}".format(round(math.sqrt(squareB), 2)))

vector_calculations(A,B)