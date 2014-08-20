# calculate number of k-permutations of n items
# bhavana harrilal
# 10 April 2014

import mymath

def main ():
   n = mymath.get_integer ("n")
   k = mymath.get_integer ("k")
   nfactorial = mymath.calc_factorial (n)
   nkfactorial = mymath.calc_factorial (n-k)
   finalanswer = nfactorial // nkfactorial
   print ("Number of permutations:", finalanswer)

if __name__ == "__main__":
   main()
