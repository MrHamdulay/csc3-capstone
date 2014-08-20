# Aaron Krishna
# 15 April 2014
# Calculate number of k-permutations of n items

def get_integer(integer): #gets integer for factorialisation (I made that word)
      n = input ("Enter "+integer+":\n") #requests user for an integer
      while not n.isdigit (): #requests until user enters an integer
            n = input ("Enter "+integer+":\n")
      n = eval (n)   
      return n


def calc_factorial(factorial): #calculates the factorial of an integer
      nfactorial = 1 
      for i in range (1, factorial + 1):
            nfactorial *= i
      return nfactorial