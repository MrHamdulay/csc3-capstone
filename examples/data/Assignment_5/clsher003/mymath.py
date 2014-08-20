"""edit question3
herman claassens
14 april 2014"""

# functiopn that promps user to enter a integer
def get_integer(x):
   if x=='n':
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n) 
      return n
   if x=='k':
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k) 
      return k
# function that calculated the factorial of a integer  
def calc_factorial(x):
   factorial = 1
   for i in range (1, x+1):
      factorial *= i   
   return factorial  
