#a program that reuse the code in the complete program to create functions required
#Jenny Luo
#16 april 2014

#define the function that converts a string input from the user into an integer
   
def get_integer(a):  
   if a == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n) 
      return n   # return the evaluated value of n
   elif a == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k) 
      return k   # return the evaluated value of k

#calculate the factorial of n
def calc_factorial(n): 
      nfactorial = 1
      for i in range (1, n+1):
         nfactorial *= i
      return nfactorial
      
   
#calculate the factorial of b, i.e. n-k 
def calc_factorial(b):
      nkfactorial = 1
      for i in range (1, b+1):
         nkfactorial *= i      
      return nkfactorial