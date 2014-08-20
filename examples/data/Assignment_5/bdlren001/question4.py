# A program to draw up the text based mathematical functions
# Budeli Rendani
# BDLREN001
# 16/04/2014

import math
def main():
    q=input("Enter a function f(x):\n") # Requesting for input from the user with q representing the function
    for y in range(10,-11,-1): # formation of the y-axis
        for x in range(-10,11,1): # formation of the x-axis by looping it through the y-axis
            z=eval(q) # Converting string to an integer and 
            s=round(z) #rounding values to whole numbers inorder to get the intercepts
            if y==s: # the function is equal to y
                print("o",end="")
            elif x==0 and y==0:
                print("+",end="") # relects the point of the origin
            elif x==0 and y!=0:
                print("|",end="") # y-xis
            elif y==0 and x!=0:
                print("-",end="") # x-axis
            else:
                print(" ",end="") #spaces for points plotted
        print()
main()
            
                
            
        
            
    