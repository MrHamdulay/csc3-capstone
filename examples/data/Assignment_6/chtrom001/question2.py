#a program to do basic vector calculations in 3 dimensions: addition, dot product and normalization
#romelon chetty
#21 april 2014

from math import *
vecA=input('Enter vector A:\n')
vecB=input('Enter vector B:\n')
x=vecA.split()
y=vecB.split()


print('A+B =', [eval(x[0])+eval(y[0]),eval(x[1])+eval(y[1]),eval(x[2])+eval(y[2])])
print('A.B =', (eval(x[0])*eval(y[0])) + (eval(x[1])*eval(y[1])) + (eval(x[2])*eval(y[2])))
print('|A| = {0:0.2f}'.format(sqrt(eval(x[0])**2 + eval(x[1])**2 + eval(x[2])**2)))
print('|B| = {0:0.2f}'.format(sqrt(eval(y[0])**2 + eval(y[1])**2 + eval(y[2])**2)))

