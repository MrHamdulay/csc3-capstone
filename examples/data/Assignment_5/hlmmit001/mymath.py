"""Question 3, Assignment 5
Mymath functions
Mitchell Holmes
14 April 2014"""

def get_integer(value):
   print("Enter",' ',value,":",sep='')
   n = input ()
   while not n.isdigit ():
      print("Enter",' ',value,":",sep='')
      n = input ()
   n = eval (n)
   return n

def calc_factorial(a):
   m = 1
   for i in range (1, a+1):
      m *= i
   return m
      

     