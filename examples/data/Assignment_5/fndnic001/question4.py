''' asci art graphing calculator
nic findlay
14 april 2014'''
import math
function = input('Enter a function f(x):\n')

for y in range(10,-11,-1):
        for x in range(-10,11,1):
                f = round(eval(function)) #for sin(x) because of decimals
                
                if f == y:
                        print("o", end="")
                elif x == 0 and y ==0 and y != f:
                        print('+', end='')
                elif x == 0 and y != 0 and y != f:
                        print('|', end='')
                elif x != 0 and y == 0 and y != f:
                        print('-', end='')
                else:
                        if y != 0 and x != 0 and y != f:
                                                print(' ', end='')
                        else: continue       
                
        print()
                                                