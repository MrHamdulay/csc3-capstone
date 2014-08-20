"""Reece Gounden
Assignment 5 Q3
"""

import math
MAX = 10
MIN = -10
output=''
sFunction = input('Enter a function f(x):\n')
xAxis = '- '*10 + '+' + ' -' *10
xAxis = xAxis.split(' ')
for y in range(MAX,MIN-1, -1):
    
    for x in range(MIN,MAX+1):
        function = eval(sFunction)
        if y==0:
            if round(function) == 0:
                xAxis[x+10] = 'o'
        else:
   
            if round(function) == y:
                output = output + 'o'
            elif x == 0:
                output += '|'
            else:
                output += ' '
    if y == 0:
        output += ''.join(xAxis)
    output += '\n'
print(output)
    
            
            
    