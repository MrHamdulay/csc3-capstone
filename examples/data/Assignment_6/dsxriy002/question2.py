#Riya Desai
#Assignment 6, Question 2
#23 April 2014

import math 

A = input("Enter vector A:\n")
splittingA = A.split(" ")
A1 = eval(splittingA[0])
A2 = eval(splittingA[1])
A3 = eval(splittingA[2])

B = input("Enter vector B:\n")
splittingB = B.split(" ")
B1 = eval(splittingB[0])
B2 = eval(splittingB[1])
B3 = eval(splittingB[2])

print("A+B = [", A1+B1, ", ", A2+B2, ", ", A3+B3, "]",sep="")

AtimesB = (A1*B1) +( A2*B2) + (A3*B3)

print("A.B =", AtimesB)


if (A1**2)+(A2**2)+(A3**2) == 0:
    Aabsolute = "0.00"
    print ("|A| =", Aabsolute)
    
else:
    Aabsolute = math.sqrt((A1**2)+(A2**2)+(A3**2))
    
    AA = round(Aabsolute, 2)    
    print("|A| =", (AA))



if (B1**2)+(B2**2)+(B3**2) == 0:
    Babsolute = "0.00"
    print("|B| =", Babsolute)
    

else: 
    Babsolute = math.sqrt((B1**2)+(B2**2)+(B3**2))
    
    BB = round(Babsolute, 2)    
    print("|B| =", (BB))



