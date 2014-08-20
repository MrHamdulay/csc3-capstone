'''drawing a graph
nicole henning
due 17 april'''

import math
function = input("Enter a function f(x):\n")


for y in range (-10,11):
     y=-y #swop since otherway around
     
     for x in range (-10, 11):
          x=int(x)
          
          if y == round(eval((function))): #eval the input string
               print ("o", end ="")
          elif x==0 and y==0:
               print ("+",end="")
          elif x == 0:
               print ("|",end="")
          elif y == 0:
               print ("-",end="")
          else:
               print (" ",end="")   

     print ()
