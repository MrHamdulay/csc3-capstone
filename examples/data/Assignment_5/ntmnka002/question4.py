f = input('Enter a function f(x):\n')

import math

for y in range(10, -11, -1):
    cart = ''
    
    for x in range(-10, 11):
        fx = eval(f)
        
        val = round(fx,0)
        if y == val:
            cart += 'o'        
        elif (x == 0) and (y == 0):
            cart += '+'
        elif (x == 0) and (y != 0):
            cart += '|'
        elif (x != 0) and (y == 0):
            cart += '-'
        else:
            cart += ' '
            
    print(cart)