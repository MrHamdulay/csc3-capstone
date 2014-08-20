#Shivam Ragoonaden
#Graph plotter

import math
#input as a string
f = input("Enter a function f(x):\n")

for y in range(-10,11):
    y *= -1    #To reflect the graph to compensate for range starting at negative
    for xi in range(-10,11):
        x=xi   #Substitute the current index of x into the equation as the value of x
        
        rf=round(eval(f)) #Convert and round function, value of x above will be subbed into the equation
#Graph        
        if rf == y:  #if rounded function, where x is the value of x index substituted, is equal to the index of y
            print("o",end="")

#Axes  
        #Y-axis
        #Ensure y index is not 0 (We don't want "|" at the origin) and that x is 0
        if y !=0 and x == 0 and  y !=rf:  #Ensure graph isn't cutting axis 
            print("|",end="")
        #Origin - When x and y indexes are both 0
        if  x== 0   and y == 0 and y != rf: #Ensure function isn't cutting the origin
            print("+", end="")
        #X-axis
        #Ensure x index is not 0 (We don't want "-" at the origin) and that y is 0        
        if y == 0 and x != 0 and y!= rf:  #Ensure function isn't cutting axis
            print("-",end="")
        
            
#Spacing            
        if y != 0 and x != 0 and y!=rf:   #If it is not the function, axis, origin, ie. everything else is space
            print(" ",end="")  
    print() #Next line