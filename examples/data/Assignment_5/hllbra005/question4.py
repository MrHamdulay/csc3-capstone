#Assignment 5: Question 4, Graph Plotting
#Brandon Hall (HLLBRA005)
#17/04/2014

import math

def Main():
    
    print("Enter a function f(x):")
    function = input()
    
    calculate(function)
    
def calculate(function):

    position = function.find("x")
    a = [] #Creates a list to store string expression with the value of "x" subbed in, later eval is used to calculate the actual value of the expression
   
    for i in range(-10,11):
        
        if(position != -1):
           
            a.append(function.replace("x", "(" + str(i)+ ")"))
        
        else:
            
            a.append(function) #Sets each value in the list equal to the function
        
                
           
    for y in range(-10,11):                        #loops check for when the value of the function equals the current value for y in the loop and then if it does it prints out an "o" and if it doesnt it prints a space. The spaces give us the gradient "m" of our graph
        
        for x in range(-10,11):
            
            b = 0 
            r = eval(a[x+10])%1
            
            if(r == 0):  #This checks to see if the number is whole or not so that it can round it off to plot
                
                b = eval(a[x+10])
                
            else:   
                if(r >= 0.5):
                    b = math.ceil(eval(a[x+10])) #This rounds up
                elif(r<0.5):
                    b = math.floor(eval(a[x+10])) #This rounds down
                   
            
            if(b == (-y)): 
                
                print ("o", end = "")  #Prints the o character where there is a plotted point
                
            elif(y!=0):
                
                if(x == 0) and (b != (-y)) :
                    print("|", end = "")#Printed on the y-axis while there is no plotted point there
                
                else:  
                    print(" ", end = "")   #Prints a space where there isnt a plotted point, this keeps the graphs gradiant 
                
           
            
            if (y == 0): #When the outer loop is at 0 i.e when the graph is on the x axis
        
                if( (x == 0) and (y == 0) and (b!= (-y))):
                    
                    print("+" ,  end = "") #Printed at the origin while there is no plotted point there
            
                elif((b != (-y))):    
                    
                    print("-", end= "")  #Printed on the x-axis while there is no plotted point there 
                
  
        print() #This prints a new line at the end of the y loop, this simulates moving down by one line each time in  a graph. i.e going down one y value at a time   
                
          
                 

Main()    