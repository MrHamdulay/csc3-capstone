import math
x=math.sqrt(2)
a=2 
while 2/x != 1:
    a=a*(2/x)
    x=math.sqrt(2+x)

print('Approximation of pi:',round( a,3))

r=eval(input('Enter the radius:\n'))
z=(r**2)*a

print('Area:',round(z,3) )





    

