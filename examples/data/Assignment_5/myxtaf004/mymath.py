# calculate number of k-permutations of n items
# tafadzwa moyo
# 14 april 2014
def get_integer (a): #Gets the integers from user
   n = input ("Enter "+a+":\n")
   while not n.isdigit ():
      n = input ("Enter "+a+":\n")
   n = eval (n)   
   return n

def calc_factorial (a): #processes intergers and gets factorial
   nfactorial = 1
   for i in range (1, a+1):
      nfactorial *= i
   return nfactorial