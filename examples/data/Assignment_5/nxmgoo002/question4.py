"""This is a question4.py which prints any functional graph
Nxumalo Goodman
18 April 2014"""

import math 
x=0
expression=input('Enter a function f(x):\n')
 
for y in range (10,-11,-1):
      for x in range (-10, 11):
            expression_given=eval(expression)
            y_real = -y/10
            #this part of the programm finds where x values is equal to y values
            if x == 0 and y == round(expression_given):
                  print ('o',end='')
                  
            elif y == 0 and y == round(expression_given):
                  print('o', end='')  
                   
            elif round(expression_given) == y:
                  print('o',end='')
                  
            # Thi part of the programm prints the graph plane
            
            elif x==0 and y==0:
                  print('+', end='')
                  
            elif x==0:
                  print('|',end='')
                  
            elif y==0:
                  print('-', end='')
                  
            else:
                  print (' ',end='')   
      print ()
     