import math

function = input('Enter a function f(x):\n')
for y in range(10,-11,-1):
    for x in range(-10,11):
        new_function = round(eval(function))
        if new_function == y:
            print('o', end = '')
        elif new_function != y and y != 0 and x !=0:
            print (' ',end= '')
        elif x == 0 and y == 0 and new_function != y:
            print ('+', end = '')
        elif x == 0 and new_function != y:
            print ('|', end = '')
        elif y == 0 and new_function !=y:
            print('-', end = '')
    print ()