def vector():
    A = []
    B = []
    import math
    # This line splits the input and creates list 1
    a = input("Enter vector A:\n")
    x = 0
    for x in a.split():
        if x == " ":
            jinx = 0 #programme should do nothing if x = " "
        elif x != " ":
            x = int(x)
            A.append(x)
        x = 0
    
    #This line splits the input and creates list 2
    b = input("Enter vector B:\n")
    y = 0
    for y in b.split():
        if y == " ":
            jinx = 0 #programme should do nothing if x = " "
        elif y != " ":
            y = int(y)
            B.append(y)
        y = 0
    
    # this next line adds the vectors
    ADD = []
    for x in range (3):
        Add_Vect = A[x] + B[x]
        ADD.append(Add_Vect)
    print ("A+B =", ADD, sep=" ")
    
    # This line calculates the dot product
    DOT = []
    for x in range (3):
        Dot_Vect = A[x]*B[x]
        DOT.append(Dot_Vect)
    FinalDot= DOT[0] + DOT[1] + DOT[2]
    print ("A.B =",FinalDot)
    
    # this line calculates the normalization
    NORM1 = []
    for x in range (3):
        Norm_Vect1= A[x]**2
        NORM1.append(Norm_Vect1)
    FinalNorm = NORM1[0] + NORM1[1] + NORM1[2]
    SFN = math.sqrt(FinalNorm)
    if SFN == 0:
        print ("|A| = ", round(SFN,1),"0",sep="")
    else:    
        print ("|A| =", round(SFN,2)) 
    
    # this line calculates the normalization
    NORM2 = []
    for x in range (3):
        Norm_Vect2= B[x]**2
        NORM2.append(Norm_Vect2)
    FinalNorm2 = NORM2[0] + NORM2[1] + NORM2[2]
    SFN2 = math.sqrt(FinalNorm2)
    if SFN2 == 0:
        print ("|B| = ", round(SFN2,1),"0", sep="")
    else:
        print ("|B| =", round(SFN2,2))     
    
vector()
             