"""calculate sine and draw graphs
hussein suleman
31 march 2014"""

import math

def sine (x):
   """calculate sine of x (where x is in radians"""
   sum = 0
   num = x
   den = 1
   den_base = 1
   epsilon = 0.00000001
   sign = 1

   while num/den > epsilon:
      sum += sign * (num/den)
      num *= x*x
      den_base += 2
      den *= den_base * (den_base-1)
      sign *= -1
      
   return sum   

def sine_graph ():
   """draw a graph of the sine function"""
   yinc = 1/24
   for y in range (-12,13):
      got_x = False
      for x in range (0, 401):
         x_real = x/400 * math.pi*2
         y_real = -y/12
         if y_real-yinc <= sine(x_real) <= y_real+yinc:
            got_x = True
         if x % 10 == 0:
            if x_real==0 and y_real==0:
               print ("+",end="")
            elif x_real == 0:
               print ("|",end="")
            elif y_real == 0:
               print ("-",end="")
            elif got_x:
               print ("X",end="")
            else:
               print (" ",end="")   
            got_x = False   
      print ()
   
def main ():
   sine_graph ()

if __name__ == "__main__":
   main ()

