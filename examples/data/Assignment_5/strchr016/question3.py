# calculate number of k-permutations of n items
# bhavana harrilal
# 10 April 2014

def get_integer(inp):
   if inp=="n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)  
      return n
   else:
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k

def calc_factorial(inpu):
      nfactorial = 1
      for i in range (1, inpu+1):
         nfactorial *= i
      return nfactorial

def main ():
   n = get_integer ("n")
   k = get_integer ("k")
   nfactorial = calc_factorial (n)
   nkfactorial = calc_factorial (n-k)
   print ("Number of permutations:", nfactorial // nkfactorial)

if __name__ == "__main__":
   main()
