#Mbongeni Mazibuko
#MZBMBO002
#Assignment 2

import math
x=2
y= math.sqrt(2)
pi= x*2/y
pi_defined='no'

while pi_defined=='no':
    y= math.sqrt(2+y)
    term=2/y
    
    if term==1:
        print('Approximation of pi:',round(pi,3))
        r= eval(input('Enter the radius:\n'))
        print('Area:',round(pi*(r*r),3))
        pi_defined='yes'
    pi*= term