#plotting graph of input function
#wayne de jager
#15 april 2014

import math
def graph ():
   a=input("Enter a function f(x):\n")
   for y in range (-10,11):
      for x in range (-10,11):
         b=eval(a) #convert string to numerical sequence
         ypoint=-b #reverse orientation of graph
         if y==round(ypoint):
            print("o",end='')
         elif x==0 and y==0:
            print("+",end="") #origin
         elif x==0:
            print("|",end="") #y-axis
         elif y==0:
            print("-",end="") #x-axis
         else:
            print(" ",end="") #empty plane co-ords
      print()
graph() #call function