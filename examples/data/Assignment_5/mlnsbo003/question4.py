'''Graph plotter
Sbongakonke Mlangeni
16 April 2014'''

import math



def graph():
    '''input'''
    fx = input('Enter a function f(x):\n')
    '''The range and domain'''
    for y in range(10,-11,-1):
        for x in range(-10,11,1):
            
            
            if y==round(eval(fx)):
                print('o' , end='') #actual graph
            elif (x == 0) and (y == 0): #Origin
                print('+' , end = '')
            elif x == 0 and y != 0:   #Y intercept
                if y == round(eval(fx)):
                    print('o' , end = '')
                else:
                    print('|' , end='') #Y axis
            elif y == 0 and x != 0:
                print('-' , end='') #X axis
            else:
                print(' ' , end='')
        print()
            
graph()
                
                
                    
            