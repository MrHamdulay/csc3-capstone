"""mymath"""
def main():
   n = eval(input ("Enter n:\n"))
   k = eval(input ("Enter k:\n"))
   n = get_integer ("n")
   k = get_integer ("k")
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   nkfactorial = 1
   for i in range (1, n-k+1):
      nkfactorial *= i
   print ("Number of permutations:", nfactorial // nkfactorial)


   
