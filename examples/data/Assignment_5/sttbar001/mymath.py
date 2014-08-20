# calculate number of k-permutations of n items
# barak setton

def get_integer(letter):
   if letter == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      return (eval (n))   
   if letter == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      return( eval (k))
      
def calc_factorial(n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return (nfactorial)

