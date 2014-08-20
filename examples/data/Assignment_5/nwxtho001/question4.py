import math

func = input ('Enter a function f(x):\n')

for j in range (10, -11, -1):
    for i in range (-10, 11):
        x = i
        if j - .5 <= eval (func) <= j + 0.5:
            print ('o', end = '')
        elif j == 0 and i == 0:
            print ('+', end = '')
        elif i == 0:
            print ('|', end = '')
        elif j == 0:
            print ('-', end = '')
        else:
            print (' ', end = '')
    print ()