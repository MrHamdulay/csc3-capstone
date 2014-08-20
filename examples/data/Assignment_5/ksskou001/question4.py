'''This program draws a text-based graph of a mathematical function f(x)
with both range and domain (-10,10)
Kouame KOUASSI
12 april 2014'''

import math
def f_graph():
         
         #get the function
         f = str(input('Enter a function f(x):\n'))
         
         for y in range (-10,11):
                  for x in range (-10, 11):
                           #y_real starts from 10 to -10
                           y_real = -y
                           
                           '''print the points of the graph  using eval to calculate the value of f(x) and round it off before the axis to get the points of interceptions rather than the axis'''
                           if y_real == round(eval(f)):
                                    print ("o",end="")
                           
                           #print the origin and the axis 
                           elif x==0 and y_real==0:
                                    print ("+",end="")
                           elif x == 0:
                                    print ("|",end="")
                           elif y_real == 0: 
                                    print ("-",end="")

                           #stay on the same line to print all the points there
                           else:
                                    print (" ",end="")
                  #get to the next line
                  print()
   
def main ():
         f_graph ()

if __name__ == "__main__":
         main ()

