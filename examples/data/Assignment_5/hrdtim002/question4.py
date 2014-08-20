"""Draw a text-based graph of f(x)
Tim Hardie
16-4-14"""

import math
function = input ("Enter a function f(x):\n")

for y in range (10,-11,-1):
    for x in range (-10,11):
        if (round (eval (function)) == y):
            print ('o', end='')
        elif (x==0 and y==0):
            print ('+', end='')
        elif (x==0):
            print ('|', end='')
        elif (y==0):
            print ('-', end='')
        else:
            print (' ', end='')
        #print('(' , x , ';' , y , ')')
    print()