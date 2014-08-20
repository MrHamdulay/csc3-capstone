# calculate number of k-permutations of n items
# bhavana harrilal
# 10 April 2014

from mymath import *

def main ():
   n = get_N ()
   k = get_K ()
   nfactorial = calc_factorial1 (n)
   nkfactorial = calc_factorial2 (n,k)
   print ("Number of permutations:", nfactorial // nkfactorial)

if __name__ == "__main__":
   main()