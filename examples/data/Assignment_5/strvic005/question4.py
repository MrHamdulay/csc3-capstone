'''draw a graph of the fuction
Victoria Stark
15 April 2014'''



import math

f=input("Enter a function f(x):\n")
           
#make a y increment as values may not be exactly on the number (may be a fraction) but will still need to be shown on the graph          
yinc = 2/20

#iterate through all values of y and x
for y in range(-10,11):
    
    for x in range(-10,11): #create loop for x going from -10 to 10
        
        x_real=round(eval(f))
        y_real=-y
        
        if x==0 and y_real!=0 and x_real!=y_real: #when x=0, we need to show the axis
            print('|', end='')                                                      
        if y_real==0 and x!=0 and x_real!=0: #when y=0, we need to show the axis
            print('-', end='')
        if y_real==0 and x==0 and x_real!=y_real: #the intercept of the x and y axis
            print('+', end='')
        if y_real==x_real: #where the points are
            print('o', end='')
        if x_real!=y_real and x_real!=0 and y_real!=0:
            print(' ', end='')
            
    print()
            
            
            