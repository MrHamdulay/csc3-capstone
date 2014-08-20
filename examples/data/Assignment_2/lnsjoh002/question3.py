# Program to calculate PI
import math





def PI():
    picalc=2
    number=0 
    Next_Term = 2
    while  Next_Term != 1:
                      
        number=math.sqrt(2+number)
        Next_Term = 2/number
        picalc = picalc*Next_Term
     
    picalcR=round(picalc, 3)    
    print("Approximation of pi:",picalcR)
    r= eval(input("Enter the radius: \n"))
    Area = picalc *r*r
    Area=round(Area,3)
    print("Area:",Area)

PI()    
    
    