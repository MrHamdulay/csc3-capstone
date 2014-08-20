""" Program to work out permutations
Richard Marais
14 April 2014"""

def get_integer(a): #get a value for n
   
   n = (input("Enter "+a+":\n"))
   if n.isdigit():
      if eval(n) >= 0:
         return eval(n) 
   else:
      get_integer(a)
      

def calc_factorial(b):   #work out the factorial of values from 'get_integer'
   
   for i in range (1,b):
      b*=i
   return b 

