#Drawing graphs
#Thembekani Gwegwana
#April

import math
def graph():
    userfunction=input('Enter a function f(x):\n')
    for y in range(10,-11,-1):
        for x in range(-10,11):
            function = eval(userfunction)
        #Drawing the axes of a graph
        
            if y==int(round(function)):
                print('o',end='')
            elif x==0 and y==0:
                print('+',end='')
            elif y==0:
                print('-',end='')
            elif x==0:
                print('|',end='')
            
            else:
                print(' ',end='')
        print()
graph()