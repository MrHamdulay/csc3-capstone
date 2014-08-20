#Question 3: Find number of permutations
#Jennifer Yuan
#16 April 2014

def get_integer(s):
      n = input ("Enter "+s+":\n") #Changes "s" according to string parameter
      while not n.isdigit (): #Continues to ask until s is a number
            n = input ("Enter "+s+":\n")
      n = eval (n) #Makes string a number
      return n


def calc_factorial(n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i #l=multiplying nfactorial by i --> accumulator
   return nfactorial

