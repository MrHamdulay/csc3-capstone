'''Lungelo Mdunge
Assignment 5, mymath'''
def get_integer(x):
   n = ''
   while not n.isdigit ():
      n = input ("Enter "+x+":\n")
   return int(n)
      
def calc_factorial(x):
   
   nfactorial = 1
   for i in range (1,x + 1):
      nfactorial *= i 
   return nfactorial
   
