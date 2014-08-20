#Emile McLennan
#Q4
#16/4/14
#Logic used from Hussein's Class Example 

import math

f=input("Enter a function f(x):\n")
           
yinc = 2/20


for y in range(-10,11):
    
    for x in range(-10,11):
        
        x_real=round(eval(f))
        y_real=-y
        
        if y_real==0 and x==0 and x_real != y_real: 
            print('+', end='')        
        elif x==0 and y_real !=x_real: 
            print('|', end='')                                                      
        elif y_real==0 and x_real!=y_real: 
            print('-', end='')
        elif y_real-yinc <= x_real <= y_real+yinc: 
            print('o', end='')
        else:
            print(' ', end='')
            
    print()