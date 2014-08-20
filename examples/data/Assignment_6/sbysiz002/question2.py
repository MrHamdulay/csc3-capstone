"""Sizwe Sibiya
SBYSIZ002: 21 Apr 2014
Solving for equations"""

import math
s=input('Enter vector A:\n')
x= s.split(" ")
p=input('Enter vector B:\n')
y= p.split(" ")

#equations for calculations
Sum = [(int(x[0])+int(y[0])),(int(x[1])+int(y[1])),(int(x[2])+int(y[2]))]
Product= ((int(x[0])*int(y[0]))+(int(x[1])*int(y[1]))+(int(x[2])*int(y[2])))
root1 = math.sqrt((int(x[0])**2) + (int(x[1])**2) + (int(x[2])**2))
root2 = math.sqrt((int(y[0])**2) + (int(y[1])**2) + (int(y[2])**2))

#returning answers to each equation for gibin values
print('A+B =',Sum)
print('A.B =',Product)
print('|A| =','{0:.{1}f}'.format(root1, 2))
print('|B| =','{0:.{1}f}'.format(root2, 2))
