"""mymath
alexander whiting
18 april 2014"""

import math
func = input("Enter a function f(x):\n")

   
ylil = 10/20
for y_real in range (10,-11,-1):
         for x in range (-10, 11):
                  if y_real == eval(func):
                           print ("o",end="")
                  elif  y_real-ylil <= eval(func) <= y_real+ylil:
                           print ("o",end="")                  
                  elif x==0 and y_real==0:
                           print ("+",end="")
                  elif x == 0:
                           print ("|",end="")
                  elif y_real == 0:
                           print ("-",end="")
                  
                           
                  else:
                           print (" ",end="")   
         print ()
   
