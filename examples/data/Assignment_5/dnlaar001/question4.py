# programe that graphically illustrates functions 
# Aaron Daniels
# 15 April 2014

import math
f=input('Enter a function f(x):\n')
for e in range(10,-11,-1):
    for x in range(-10,11):
        #d=f.replace('x',str(k))
        h=eval(f)
        s=round(h)
         
        if s==e:
            print('o',end='')
        elif e==0 and x==0:
            print('+',end='')
        elif x==0:
            print('|',end='')
        elif e==0:
            print('-',end='')
        else:
            print(' ',end='')    
    print()