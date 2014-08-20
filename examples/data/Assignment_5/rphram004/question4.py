"""question4: programme to print out certain graphs after prompted for an input
#rama raphalalani
#15-04-2014"""

import math #brings in maths library
x=0
functions=input("Enter a function f(x):"'\n')
#loop runs with the parameters given by the question.
for y in range (10,-11,-1):
      for x in range (-10, 11):
            function = eval(functions)

            y_real = -y/10
            if x==0 and y==round(function):
                  print ("o",end="")
            elif round(function)==y:
                  print("o",end="")
            elif y==0 and y==round(function):
                  print("o", end="")
                  
            #prints the origin      
            elif x==0 and y==0:
                  print("+", end="")
             
            #prints the y-axis needed for the graph     
            elif x==0:
                  print("|",end="")
                  
           #prints the x-axis needed for the graph
            elif y==0:
                  print("-", end="")
            else:
                  print (" ",end="")   
      print ()
     