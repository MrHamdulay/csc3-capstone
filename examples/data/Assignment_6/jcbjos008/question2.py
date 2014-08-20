'''Joshen Credelio Jacob
mathematic functions
21/04/2014'''
import math

#creating a list
vect_A = input('Enter vector A:\n')
vect_B = input('Enter vector B:\n')
vect_A = vect_A.split()
vect_B = vect_B.split()

#addition function
add = []
for i in range(len(vect_A)):
    x=eval(vect_A[i])
    y=eval(vect_B[i])
    z = x +y
    
    add.append(z)

print('A+B =',add)

#product function
a=0
for i in range(len(vect_A)):
    x=eval(vect_A[i])
    y=eval(vect_B[i])
    z = x*y
    a = a+z
print('A.B =',a)

#power function
b=0
for i in range(len(vect_A)):
    x=eval(vect_A[i])
    z=x**2
    b+=z
b='{0:.2f}'.format(round(math.sqrt(b), 2))
print('|A| =',b)

c=0
for i in range(len(vect_A)):
    y=eval(vect_B[i])
    z=y**2
    c+=z
c='{0:.2f}'.format(round(math.sqrt(c),2))
print('|B| =',c)
