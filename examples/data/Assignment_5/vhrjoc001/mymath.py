#jocelyn
# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

#function to enter a digit
def get_integer(n):
   a = input ("Enter "+n+":"+"\n")
   while not a.isdigit ():
      a = input ("Enter "+n+":\n")
   a = eval (a)   
   return a


#function to create a factorial
def calc_factorial(n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial




