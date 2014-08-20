"""Program to print mathematical functions
Geoff Murphy
MRPGEO001
16 April 2014"""

import math

function = input("Enter a function f(x):\n")              #The mathematical function is entered
function_val_x = ""                                       #Initial value

def graph ():
   global function                                        #'global' allows 'function' and 'function_val_x' to be used inside and outside of the graph function
   global function_val_x   
   for y_val in range (-10,11):
      for x_val in range (-10, 11):
         x = str(x_val)
         function_val_x = function                             #Takes entered function...
         function_val_x = function_val_x.replace('x','(x)')    #Replaces all all occurences of 'x' withs (x) for mathematical purposes...
         function_val_x = function_val_x.replace('x',x)        #And then replaces new x's with the current x value from the for loop.
                             
         x = round(eval(function_val_x))                       #The function is then turned into a numerical answer and rounded off. (This is x's final answer)               
         y = -y_val                                            #Because of the nature of the programming, the y-values need to be inverted (This is also f(x)'s answer)
         
         
         #Checks the various x and y values and decides whether a point should be plotted (with a 'o')
         if x_val == 0 and y_val == 0 and y != x:              #If the point is the origin
            print ("+",end="")
         elif x_val == 0 and y_val == 0 and x == y:            #If a plotted point lies on the origin
            print ("o",end="")
         elif x == 0 and y == 0:                               #If a plotted point lies anywhere that's not on the axes
            print("o",end="")
         elif x_val == 0 and y != x:                           #If it is the vertical axis and no point lies on it
            print ("|",end="")
         elif x_val == 0 and y == y_val:                       #If a plotted point lies directly on the vertical axis
            print("o",end="")
         elif y_val == 0 and x == y:                           #If a plotted point lies directly on the horizontal axis
            print("o",end="")         
         elif y == 0:                                          #If it is the horizontal axis and no point lies on it
            print ("-",end="")
         elif y == x:                                          #If the plotted point lies anywhere else on the cartesian plane other than on the axes
            print ("o",end="")
         else:
            print (" ",end="")   
      print ()
      
graph()
   