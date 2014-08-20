#Program to draw graphs
#Denzel Ncube
#15 April 2014

#import the math module
import math

# Function to calculate the y value when given the x value and a formula
def calcY(x,formula):
    yvalue = round(eval(formula.replace("x","("+str(x)+")")))
    return yvalue
#Function to draw the graph
def drawgraph():
    #Getting input
    form = input("Enter a function f(x):\n")    
    #Setting the increment
    yincrement = 1/10
    #Setting the range of x and y
    for y in range(-10,11):
        for x in range(-10,11):
            xblock = -x
            yblock = -y
            #Plotting the points
            if round(yblock-yincrement) == calcY(x,form) == round(yblock+yincrement):
                print ("o",end="")            
           #Plotting the origin
            elif xblock==0 and yblock==0:
                print ("+",end="")
           #PLotting y axis
            elif xblock == 0:
                print ("|",end="")
           #PLotting x axis
            elif yblock == 0:
                print ("-",end="")
            #PLotting the blank spaces
            else:
                print (" ",end="")      
        print ()            
    
def main ():
    drawgraph ()

if __name__ == "__main__":
    main ()

            

        
        

