"""Graph plotter
Charlie Shang 15 April 2014
SHNHUA002"""

import math
MAX = 10 #set the domain of the graph
MIN = -10
output=''
sFunction = input('Enter a function f(x):\n')
xAxis = '- '*10 + '+' + ' -' *10 # draws the x axis in a temp variable
xAxis = xAxis.split(' ') #split the x axis into a set so that characters in specific positions can be altered
for y in range(MAX,MIN-1, -1): #vertical
    
    for x in range(MIN,MAX+1):#horizontal
        function = eval(sFunction)
        if y==0: #for the point of the function which lies on the x axis
            if round(function) == 0:
                xAxis[x+10] = 'o'
        else:
   
            if round(function) == y: #if the function = the current y value in the loop, plot a point
                output = output + 'o'
            elif x == 0:
                output += '|'
            else:
                output += ' '
    if y == 0: #plots the x axis when y = 0
        output += ''.join(xAxis) 
    output += '\n'
print(output)
    
            
            
    