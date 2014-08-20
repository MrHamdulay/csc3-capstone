#program to calculate the number of n permutations
#KNNSAD001

from mymath import *

#define program
def main ():
   
   #prompts program to use math library
   a = get_integer ("n")
   b = get_integer ("k")
   afactorial = calc_factorial (a)
   abfactorial = calc_factorial (a-b)
   print ("Number of permutations:", afactorial // abfactorial)

if __name__ == "__main__":
   main()
