""" Bella Gorham
altered given code to make mymath
14/04/2014"""

#function for input
def get_integer(x):
   print("Enter ",x,":\n",sep="",end="")
   p = input ()
   while not p.isdigit ():
      print("Enter ",x,":\n",sep="",end="")
      p = input ()
   num = eval(p) 
   return num


#funtion to get factorial
def calc_factorial(x):
   n1factorial = 1
   for i in range (1, x+1):
      n1factorial *= i
   return n1factorial


     
