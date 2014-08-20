# calculate number of k-permutations of n items
# ARNTYR001
# 17 April 2014

def get_integer_n():
   n = input ("Enter n:\n")
   while not n.isdigit ():
      n = input ("Enter n:\n")
   n = eval (n)  
   return n

def get_integer_k():
   
   k = input ("Enter k:\n")
   while not k.isdigit ():
      k = input ("Enter k:\n")
   k = eval (k)
   return k 

def calc_factorial_n(n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial

def calc_factorial_k(n,k):
   nkfactorial = 1
   for i in range (1, n-k+1):
      nkfactorial *= i   
   return nkfactorial

def main ():
   n = get_integer_n()
   k = get_integer_k()
   nfactorial = calc_factorial_n (n)
   nkfactorial = calc_factorial_k (n,k)
   print ("Number of permutations:", nfactorial // nkfactorial)

if __name__ == "__main__":
   main()
