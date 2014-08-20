#Question 4
#Adam Rosendorff-RSNADA001
#15/04/2014

import math

function = input('Enter a function f(x):\n')

for y in range(-10,11):
    for x in range(-10,11):
        done = False
        if round(eval(function)) == -y:
            print('o',end='')
        elif x == 0 and y == 0:
            print('+',end='')
        elif y == 0:
            print('-',end='')
        elif x == 0:
            print('|',end='')
        else:
            print(' ',end='')
    print()
