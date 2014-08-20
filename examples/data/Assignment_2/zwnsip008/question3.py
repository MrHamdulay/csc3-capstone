from math import*

y=2
s=sqrt(2)
while (2/s)!=1:
    y*=2/s
    s=sqrt(2+s)
print('Approximation of pi:', round(y,3))
m=eval(input('Enter the radius:\n'))
p=(y*m**2)
print('Area:', round(p,3)) 

       
    