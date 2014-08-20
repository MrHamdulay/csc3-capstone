# graph sketcher
# hs
# 23 march 2011

import math

fx = input ("Enter a function f(x):\n")

for y in range (10, -11, -1):
   for bx in range (-10, 11):
#      yes = 0
#      for mx in range (-49, 50):
#         x = bx+mx/100
#         if round (eval(fx)) == y:
#            yes = 1
      x = bx
#      if yes == 1:
      if round(eval(fx)) == y:
         print ("o", end="")
      elif x == 0:
         if y == 0:
            print ("+", end="")
         else: 
            print ("|", end="")
      elif y == 0:
         print ("-", end="")
      else:
         print (" ", end="")
   print ("")   
