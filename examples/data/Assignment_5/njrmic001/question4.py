#A program to draw a text-based graph of a mathematical function
#Michelle Njoroge
#15 April 2014


import math #imports the math library
def main():
    x=0
    f_of_x=input("Enter a function f(x):\n")
    yinc=0.5 #takes into account functions whose x and y values are not necessarily integer values
#loop through all the possible x values (columns) for one y value (the row)
    for y in range (10,-11,-1):
        for x in range (-10,11,1):
            function=eval(f_of_x)
            if y-yinc<=round(function)<=y+yinc:
                print ("o",end="")
            elif y!=round(function):
                if x==0 and y==0: #if it is at the origin
                    print("+", end="")                
                elif x==0: #if it is on the y-axis
                    print("|",end="")
                elif y==0: # if it is on the x-axis
                    print("-",end="")
                else: #if it is anywhere else on the grid
                    print(" ",end="")
        print() #moves to the following line after iterating through all possible x-values for one y-value
main()

        
    
    
    