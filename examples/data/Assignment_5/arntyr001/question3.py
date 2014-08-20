# calculate number of k-permutations of n items
# bhavana harrilal
# 10 April 2014

from mymath import *

def main ():
   n = get_integer_n()
   k = get_integer_k()
   nfactorial = calc_factorial_n (n)
   nkfactorial = calc_factorial_k (n,k)
   print ("Number of permutations:", nfactorial // nkfactorial)

if __name__ == "__main__":
   main()
