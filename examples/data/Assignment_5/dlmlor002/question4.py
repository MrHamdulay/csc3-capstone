"""program to draw graphs
Lorena Dal Maso
16 April 2014"""

import math

func = input("Enter a function f(x):\n")

def graph ():
   """draw a graph of the function"""
   yinc = 1
   for y in range (-10,11):
      got_x = False
      for x in range (-10, 11):
         x_real = x
         y_real = -y
         if y_real-yinc <= (x_real) <= y_real+yinc:
            got_x = True
         if x %10 == 0:
            if x_real==0 and y_real==0:
               print ("+",end="")
            elif x_real == 0:
               print ("","","","","","","","","","|",end="")
            elif y_real == 0:
               print ("-"*10,end="")
            elif got_x:
               print ("o",end="")
            else:
               print (" ",end="")   
            got_x = False   
      print ()
   
def main ():
   graph ()

if __name__ == "__main__":
   main ()