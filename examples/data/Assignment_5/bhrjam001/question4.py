import math

def graph(function):
    for y in range (10, -11, -1):
        for x in range(-10, 11):
            val = (round(eval(function)), x)
            
            if y == val[0] and x == val[1]:
                print('o', end='')
            elif y == 0 and x == 0:
                print('+', end='')
            elif y == 0:
                print('-', end='')
            elif x == 0:
                print('|', end='')
            else:
                print(' ', end='')
        print()
   
graph(input('Enter a function f(x):\n'))