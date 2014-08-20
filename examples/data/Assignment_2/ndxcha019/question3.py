#program to calculate the area of a circle

'''loop to calculate the value of pi'''
import math
a=0
num=2
pi=1
while num>1:
    pi=pi*num
    b=math.sqrt(2+a)
    a=b
    num=2/b

print('Approximation of pi:',round(pi,3))
r=eval(input('Enter the radius:\n'))
A=(r**2)*pi
A_round=round(A,3)
print('Area:',A_round)

