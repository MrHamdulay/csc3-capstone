# calculate number of k-permutations of n items
# Michael Field
# 10 april 2014

def get_integer(choice):
   
   #get n integer
   if (choice == 'n'):
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      
      return n
   
   #get k integer
   if (choice == 'k'):
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
   
      return k
      
def calc_factorial(n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   
   return nfactorial
   