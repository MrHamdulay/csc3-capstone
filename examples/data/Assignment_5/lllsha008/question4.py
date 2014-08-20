
import math

myin = input('Enter a function f(x):\n')
#getting the function

for i in range(10, -11, -1):
    #because you go from positive side to negative
    for j in range(-10, 11):
        x = j
        y = round(eval(myin))
        #find x and y values
        if i == y:
            #if we are at a value on function, print o
            print('o', end = '')
            continue
        if j == 0 and i == 0:
            #print origin character if no o
            print('+', end = '')
            continue
        if j == 0:
            #print y axis if no o
            print('|', end = '')
            continue
        if i == 0:
            #print x axis if no o
            print('-', end = '')
            continue
        #otherwise if nothing was done, print space
        print(' ', end = '')
    #add a endline character
    print('')
