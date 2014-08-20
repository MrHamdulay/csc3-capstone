"""module that calculates the number of k-permutations of n items
Matthew Finlayson - FNLMAT001
15/04/2014"""

# prompts the user to enter n, repromts if n is not a digit, returns the user's input
def get_integer(letter): 
   n = input ("Enter "+letter+":\n")
   while not n.isdigit ():
      n = input ("Enter "+letter+":\n")
   n = eval (n)
   return n

# calculates and returns the factorial of num
def calc_factorial(num):
   nfact = 1
   for i in range (1, num+1):
      nfact *= i
   return nfact
