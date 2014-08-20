""" program to calculate number of k-permutations of n items"""
#Author: Rofhiwa Liphauphau, Adapted from code provided
#Date: 16 April 2014
def get_integer(vari): 
   variable= input ("Enter "+vari+":\n")
   while not variable.isdigit ():
      variable= input ("Enter "+vari+":\n")
   variable=eval(variable)
   return variable  


def calc_factorial(variable2): #This finds the factorial for the input
   factorial = 1
   for i in range (1,variable2+1):
      factorial *= i
   return factorial

def main ():
   n = get_integer ("n")
   k = get_integer ("k")
   nfactorial = calc_factorial (n)
   nkfactorial = calc_factorial (n-k)
   print ("Number of permutations:", nfactorial // nkfactorial)

if __name__ == "__main__":
   main()