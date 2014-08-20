''' Programs that draws graph of a given function 
 Name: Othniel KONAN
 Student number: KNNOTH001
 Date: 2014/04/12'''

import math

function = input('Enter a function f(x):\n')

#nested loops to make a grid of 20*20
for y in range(-10,11):
    for x in range(-10,11):
        if round(eval(function)) == -y:                         #print 'o' if the f(x)=-y
            print('o',end='')
        elif y == 0 and x!=0 and round(eval(function)) != 0 :   #print '-' for the x-axis if f(x)!=0
            print('-',end='')
        elif x == 0 and y!=0 and round(eval(function)) != -y:   #print '|' for the y-axis if f(0)!=-y
            print('|',end='')
        elif x==y and y==0 :                                    #print '+' for x=0 and y=a if f(0)!=0
            print('+',end='')
        else:                                                   #print space for the rest of the grid
            print(' ',end='')
    print()                                                     #go to the next line for the next x_line