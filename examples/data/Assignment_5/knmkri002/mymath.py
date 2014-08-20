"""program to calculate the number of k permutations of n items
Kristin Kinmont
14 April 2014"""

def get_integer(s):
   if s == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return n
   elif s == "k":
      k = input ("Enter k:\n") 
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k
   else:
      return 0


def calc_factorial(s):
   factorial = 1
   for i in range (1, s+1):
      factorial *= i
   return factorial
   #nkfactorial = 1
   #for i in range (1, n-k+1):
      #nkfactorial *= i