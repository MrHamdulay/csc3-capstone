import math
f=input('Enter a function f(x):\n')
for y in range(-10,11):
    for x in range(-10,11):
        func=f.replace('x','('+str(x)+')')
        func = -round(eval(func))
        if y==func:
            print('o',end='',sep='')
        elif y==0 and x==0:
            print('+',end='',sep='')
        elif y==0:
            print('-',end='',sep='')
        elif x==0:
            print('|',end='',sep='')
        else:
            print(' ',end='',sep='')
        
    print()