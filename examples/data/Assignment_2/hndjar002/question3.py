# 10 March 2014
# Jaren Hendricks
# Programme to calculate pi and the area of a circle. 

import math
m=2
denom=math.sqrt(m)
pi=2 *(m/denom)
nt=0


while(True):        
        
        denom=math.sqrt(2+denom)
        nt = (m/denom)
        if(nt == 1):
                break
        else:
                pi=pi*nt
        
print ("Approximation of pi:", round ((pi),3))  
rad= eval(input("Enter the radius:\n"))
area = (pi * rad**2)
print ("Area:",round((area),3 ))