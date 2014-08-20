#drawing graphs with ascII art
#Michael Field
#14 April 2014

import math
function = input("Enter a function f(x):\n")

for y in range (-10,11):
      for x in range (-10, 11):
            
            stringx = '(' + str(x) + ')'
            
            functionValue = function.replace("x", stringx) #replace all x characters in the string 'function' with the integer x from the for loop
            
            functionValue = -eval(functionValue)
            functionValue = round(functionValue)
            
            if functionValue == y:
                  print ("o",end="")            
            
            elif x == 0 and y == 0:
                  print ("+",end="")
            elif x == 0:
                  print ("|",end="")
            elif y == 0:
                  print ("-",sep = '', end="")
            else:
                  print(' ',end = '')
                     
      print ()