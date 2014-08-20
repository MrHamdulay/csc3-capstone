# Kate Bell
# BLLKAT005
# 16 April 2014
"""Graph a function entered by user"""

import math

def graph_f():
    increment = 1/2
    
    # Prompt user to enter function
    function = input("Enter a function f(x):\n")
    
    # Loop through graph plane
    for y in range (10,-11,-1):
        for x in range (-10,11):
            
            # Find y value of function at each x value
            y_value= eval(function)
            
            # If y value of function is approximately equal to discrete point on graph, plot point
            if y_value-increment <= y <= y_value+increment: print("o",end="")
            
            # Draw axes
            elif y == 0 and x == 0: print("+",end="")
            elif x == 0: print("|",end="")
            elif y == 0: print("-",end="")
            else: 
                print(" ",end="")
        print()
        
def main ():
    graph_f()

if __name__ == "__main__":
   main ()