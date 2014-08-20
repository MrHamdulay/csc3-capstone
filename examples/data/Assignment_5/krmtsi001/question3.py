# calculate number of k-permutations of n items
# bhavana harrilal
# 10 April 2014

from mymath import * #this is used to enable the functions saved in mymath

def main ():
   n = get_integer ("n") #the get_integer fanction does as required as it was imported
   k = get_integer ("k")
   nfactorial = calc_factorial (n)#the  calc_fanction does as required as it was imported
   nkfactorial = calc_factorial (n-k)
   print ("Number of permutations:", nfactorial // nkfactorial)

if __name__ == "__main__": #this does not allow the answers of the mymath to be out on display
   main()
