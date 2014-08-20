# a program that finds the area of a circle
# Tofunmi Olagoke
# 13 March 2014
# OLGMOF001

import math
def Pi():
    apPi=2
    plusTerm=math.sqrt(2)
    while(2/plusTerm)!=1:
        apPi=apPi*(2/plusTerm)
        plusTerm=math.sqrt(2+plusTerm)
    print("Approximation of pi:", round(apPi,3)) 
    
    radius=eval(input("Enter the radius:\n"))
    Ar=apPi*radius*radius
    print("Area:" , round(Ar,3))
Pi()