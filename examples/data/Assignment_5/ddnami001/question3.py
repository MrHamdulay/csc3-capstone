# calculate number of k-permutations of n items
# bhavana harrilal
# 10 April 2014

from mymath import *

def main ():
   n = get_integer ("n")
   k = get_integer ("k")
   nfactorial = calc_factorial (n)
   nkfactorial = calc_factorial (n-k)
   print ("Number of permutations:", nfactorial // nkfactorial)



   

if __name__ == "__main__":
   main()
