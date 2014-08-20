"""question4.py text-based graph
Author : Musa Xakaza
Student# : XKZMUS001
Date : 13/04/2014"""

import math
def calcY(y,x):
   sum = eval(y)
   return sum

def sketchGraph(f):
   yinc = 10/20
   for y in range(-10,11):
      for x in range(-10, 11):
         x_real = x
         y_real = -y
         if y_real-yinc <= calcY(f,x_real) <= y_real+yinc:
            print('o',end='')
         elif y_real == 0 and x_real == 0: print('+',end='')
         #elif y_real == calcY(f,x_real): print('o',end='')
         elif x_real == 0: print('|',end='')
         elif y_real == 0: print('-',end='')
         else: print(' ',end='')
      print()

def main():
   function = input("Enter a function f(x):\n")
   sketchGraph(function)

main()  