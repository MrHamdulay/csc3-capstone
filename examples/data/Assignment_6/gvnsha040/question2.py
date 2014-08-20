list=[]
a = input('Enter vector A:\n')
b = input('Enter vector B:\n')
a=a.split(' ')

b=b.split()

c=eval(a[0])
d=eval(a[1])
e=eval(a[2])


f=eval(b[0])
g=eval(b[1])
h=eval(b[2])


one=c+f
one=str(one)
two=d+g
two=str(two)
three=e+h
three=str(three)

print('A+B = '+'['+one+','+' '+two+','+' '+three+']')

mul=c*f
mull=d*g
mulll=e*h
ans=mul+mull+mulll
print('A.B =',ans)

on=c**2

tw=d**2

th=e**2


square=on+tw+th

import math

square=math.sqrt(square)



print('%s = %.2f'%('|A|',square))


een=f**2
twee=g**2
drie=h**2

vierkant = een+twee+drie


vierkant=math.sqrt(vierkant)
print('%s = %.2f'%('|B|',vierkant))