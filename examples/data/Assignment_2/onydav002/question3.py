# value of PI

import math
c=2

v=math.sqrt(2)

b=2*(c/v)

while v<2:
    v=math.sqrt(2+v)
    b=b*(c/v)
    
print("Approximation of pi:",round(b,3))

    
def circ():
    z = eval(input("Enter the radius:\n"))
    area=round((b*z**2),3)
    print ("Area:",area)
    
circ()
    
    

    