# calculate number of k-permutations of n items
#Nic Findlay
# 10 April 2014

from mymath import *

def main ():
   n,k = get_integer()
   print ("Number of permutations:", calc_factorial(n,k))

if __name__ == "__main__":
   main()
