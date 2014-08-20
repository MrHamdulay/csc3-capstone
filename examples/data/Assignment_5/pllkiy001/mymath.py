#altered program
#kiyarah pillay 
#15 april 2014
def main ():
   n = get_integer ("n")
   k = get_integer ("k")
   nfactorial = calc_factorial (n)
   nkfactorial = calc_factorial (n-k)
   print ("Number of permutations:", nfactorial // nkfactorial)


if __name__ == "__main__":
   main()
def get_integer(a):
   if a=="n":
      b=input("Enter n:\n")
      while not b.isdigit ():
         b=input("Enter n:\n")
         return eval(b)
   elif a=="k":
      c=input("Enter k:\n")
      while not c.isdigit ():
         c=input("Enter k:\n")
         return eval(c)  