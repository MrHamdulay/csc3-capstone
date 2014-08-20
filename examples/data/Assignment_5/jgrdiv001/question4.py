"""program to draw graphs
Divan Jagers
14 April 2014"""

import math
def graph ():
   """draw a graph of a function"""
   f=input("Enter a function f(x):\n")
   for y in range (-10,11):         #ALL THE Y VALUES
      for x in range (-10, 11):      #ALL TYHE X VALUES
         if round(eval(f)) == -y:     #elauates the value entered and rounds it
            print("o",end="")
         elif x==0 and y==0:         #point where the two axes intersect
            print ("+",end="")
         elif x == 0:                #prints the y-axis
            print ("|",end="")
         elif y == 0:
            print ("-",end="")       #prints the x-axis
         else:
            print (" ",end="")        #prints nothing   
      print ()
   
def main ():
   graph ()

if __name__ == "__main__":
   main ()

