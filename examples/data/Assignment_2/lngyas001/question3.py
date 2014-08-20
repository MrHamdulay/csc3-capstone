import math
denom = 0
num = 2
pi = 1
while num > 1:
    pi = pi*num
    denom = math.sqrt(2 + denom)
    num = 2/denom
print('Approximation of pi:', round(pi,3))
r = eval(input('Enter the radius: \n'))
a = round(pi*r**2,3)
print('Area:', a) 

         