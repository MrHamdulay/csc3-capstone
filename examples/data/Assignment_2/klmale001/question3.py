import math
d=math.sqrt(2)
pi=2
while d!=2:
    pi=pi*2/d
    d=math.sqrt(d+2)

print ("Approximation of pi:",round(pi,3))
r=eval(input('Enter the radius:\n'))
a=pi*r*r
print('Area:', round(a,3))
