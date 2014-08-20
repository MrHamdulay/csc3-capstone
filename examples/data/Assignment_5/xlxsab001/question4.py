import math
f=input('Enter a function f(x):\n')
y=-10
x=-10
while -10<=y<11:
    x=-10
    while -10<=x<11:
        fx=f.replace('x','('+'x'+')')
        fx=-round(eval(fx))
        if y==fx:
            print('o',end='',sep='')
        elif y==0 and x==0:
            print('+',end='',sep='')
        elif y==0:
            print('-',end='',sep='')
        elif x==0:
            print('|',end='',sep='')
        else:
            print(' ',end='',sep='')
        x+=1
    print()
    y+=1