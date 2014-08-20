""" Graph making program, question 4
Richard Marais
14/04/14"""

import math         
def func():                           #asks for the user to enter a function
   fnc = (input('Enter a function f(x):\n'))
   graph(fnc)                         #calls graph function


def graph(fnc):             
   
   
   for y in range(10,-11, -1):                  #counting down for the y values/axis
      for x in range(-10,11):                    #nested loop for horizontal x values
         if round(eval(fnc.replace("x", ("("+str(x)+")")))) == y:      #if the value for the function calculated equals y print 'o' 
            print('o',end='')
         elif x == 0 and y == 0:      #at the origin print +
            print("+",end='')
         elif x == 0:                     #at x = 0 print the y axis marker
            print("|", end='')
         elif y == 0:
            print("-",end='')                    #print x axis
         else: 
            print(" ",end='')                #space
      print()
   
func()      
  
      


