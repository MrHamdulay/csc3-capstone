"""Program which sketches a basic graph
ARNTYR001
17 April 2014"""

import math

def main():
   f_of_x = input("Enter a function f(x):\n")
   graph_literal(f_of_x)
   
def graph_literal(f_of_x):
   y_inc = 0.5
   for y in range(10,-11,-1):
      for x in range(-10,11):
         y_real = eval(f_of_x)
         if y_real - y_inc <= y <= y_real + y_inc:
            print("o", end = "")
         elif x == 0 and y == 0:
            print("+", end="")         
         elif x == 0:
            print("|", end="")
         elif y == 0:
            print("-", end="")
       
         else:
            print(" ", end="")
      print()
      
   

if __name__ == "__main__":
   main()

