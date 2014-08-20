formula = input("Enter a function f(x):\n")
import math
for y in range (-10,11):
    for x in range (-10,11):
        y_real = -y
        stringx='('+str(x)+')'
        realformula = formula.replace('x',stringx)
        x_real = eval(realformula)
        if round(x_real)==y_real:
            print('o',end='')
        elif y==0 and x==0:
            print('+',end='')
        elif y==0:
            print('-',end='')
        elif x==0:
            print('|',end='')
        else:
            print(' ',end='')
    print()
        
        