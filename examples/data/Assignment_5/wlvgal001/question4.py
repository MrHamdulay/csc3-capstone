#text-based graph builder: Question 4 
#galya Wolov
#16 April 2014
import math

#importing math allows the user to use any function
fy=(input("Enter a function f(x):\n"))

#prints the y from top to bottom- postive to negative
for othery in range (10,-11,-1):
     #this is necessary to follow the example
     if othery!= 10:
          print('')
     #we need to go from left to right  -negative to postive and range does not write the last one     
     for x in range (-10,11):
          realy= eval(fy)
          realy1=round(realy)
          #the above ensures that the program prints discreet values only
          #this is to draw the origin
          if othery ==0 and x==0 and realy1 != 0:
               print("+",end='') 
          #program uses realy1 !=0 to ensure that the dashes and lines are only printed if graph is not plotted to lie on axes   
          elif othery ==0 and realy1 != 0:
               print("-", end='')
               
          elif x==0 and realy1 != othery:
               print("|", end='')          
          #plots the points
          elif othery == realy1:
               print("o", end='')          
          #plots the neccessary space in the graph 
          else: print(" ",end='')

