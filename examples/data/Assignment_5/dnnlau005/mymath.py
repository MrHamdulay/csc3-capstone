"""calculate number of k-permutations of n items
Lauren Denny
17 april 2014"""


def get_integer(n):
   """asks for an integer, sets the given variable name as that integer, then returns the integer"""
   inputstr = "Enter "+ n + ":\n"
   n = input (inputstr)
   while not n.isdigit ():
      n = input (inputstr)
   n = eval(n)
   return n   
      
def calc_factorial(n):
   """returns n! for a given integer"""
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial

