#Mbongeni Mazibuko
#MZBMBO002
#Assignment 5

import math
function= input('Enter a function f(x):\n')

for y in range(-10,11):
    for x in range(-10,11):
        fx= list(function)
        for j in range(len(function)):
            if fx[j]=='x':
                fx[j]='('+str(x)+')'
            f= round(eval("".join(fx)))
    #print(str(f))

        if x==0 and x!=10 and y!=0 and -y!=f:
            print('|',end='')
        elif x!=0 and y!=0 and -y!=f:
            print(' ',end='')
        if x==10 and y!=0 and -y!=f:
            print('')
        if x==0 and y==0 and -y!=f:
            print('+',end='')
        if y==0 and -y!=f and x!=0:
            print('-',end='')
        if y==0 and x==10 and -y!=f:
            print('')
        if -y==f:
            print('o',end='')
        if -y==f and x==10:
            print('')
            
"""test with:
x+2
x
5
x**2+1
0.2*x**2 -3
math.sin(x/2)*2"""