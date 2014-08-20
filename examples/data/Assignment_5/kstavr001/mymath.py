#Assignment 5, Question 3
#Avreyna Kistensamy
#14 April 2014

#define function to get integer from user
def get_integer(x):
   if x == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return n
   elif x == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k

#Definining function to calculate the factorial of n
def calc_factorial (n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial

#Defining a function to return factorial of d
def cal_factorial (d):
   nkfactorial = 1
   for i in range (1, d+1):
      nkfactorial *= i
   return nkfactorial


