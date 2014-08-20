"""Drawing graphs
Jordan Kadish 16 April 2014
imported modules: math"""
import math
#yinc=2/20
y=input('Enter a function f(x):\n')
for height in range (10,-11,-1):
    if height!=10:
        print('')
    for x in range(-10,11):
        equation=eval(y)
        function=round(equation) #rounded the input to make sure the graph touches
        if function==height:
                    print('o',end='')        
        elif x==0 and height==0:
                    print('+',end='')
        elif height==0:
            print('-',end='')        
        elif x==0:
            print('|',end='')
        else:
            print(' ',end='')