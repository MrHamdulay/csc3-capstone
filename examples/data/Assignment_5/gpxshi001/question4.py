#GPXSHI001
#17th April
#Q4

import math

function=input("Enter a function f(x):\n")
#Create axes

for i in range(10,-11,-1):
    
    for j in range(-10,11):
        x = j
        y = round(eval(function))
        
        if y == i:    
            print("o", end = "")
            
        elif(j==0 and i == 0):
            print('+',end = '')
            
        elif(i==0):
            print('-', end = '')   
            
        elif(j==0):
            print('|', end = '')
            
        else:
            print(' ',end = '')
        
            
    print()