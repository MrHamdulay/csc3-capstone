"""Draw graph from user input
Telisha Ramlall
12/04/2014"""

import math

x = 0
y = 0

#Get equation from user
equation = input("Enter a function f(x):\n")

#Plot points on graph that lie on graph
for i in range(10,-11,-1):
    
    for k in range(-10,11):
        
        x = k #give x a numerical value
        y_value = round(eval(equation)) #find y value of function
        
        if y_value == i:
            print("o", end = "") #print o if point on function
            
        if i == 0 and k == 0 and  i != y_value:
            print("+", end = "") #print (0, 0) co-ordinate
            
        if k == 0 and i != 0 and i != y_value:
            print("|", end = "") #Print verticle axis
            
        if i == 0 and  k!=0 and  i != y_value:
            print("-", end = "") #Print horizontal axis
            
        elif i != 0 and k != 0 and i != y_value:
            print(" ", end = "") #End of run-time
            
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   