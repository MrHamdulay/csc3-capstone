# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014
#Adapted by Guy Green
#For assingment

#Getting an integer from user
def get_integer(n):
   a = input ("Enter "+n+":"+"\n")
   while not a.isdigit ():
      a = input ("Enter "+n+":"+"\n")
   a = eval (a) 
   return a

#Calculating factorial for the integer
def calc_factorial(n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial

