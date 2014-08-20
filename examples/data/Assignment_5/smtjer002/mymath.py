"""A programme to provide functions to calculate permutations
by Jeremy Smith SMTJER002
14 April 2014"""

#function to get an integer as an input
def get_integer(a):
   print("Enter ",a,":", sep="")
   x = input()
   while not x.isdigit ():
      print("Enter ",a,":", sep="")
      x = input()
   x = eval(x)
   return x

#function to calculate the permutations of the factorials of two integers
def calc_factorial(a):
   nfactorial = 1
   for i in range (1, a+1):
      nfactorial *= i
   
   return nfactorial





