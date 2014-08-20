''' Phillip Ruhesi
this program calculates the number of permutations for given input
17/04/14'''
def get_integer (n):                      #defines the function get_integer so it can be called in future
      s = input ("Enter "+n+":\n")
      while not s.isdigit ():
            s = input ("Enter "+n+":\n")
      n = eval (s)   
      return n

def calc_factorial (n):
      nfactorial = 1                      #defines the function calc_factorial so it can be called in future
      for i in range (1, n+1):
            nfactorial *= i
      return nfactorial

