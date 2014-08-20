#Permutations
#Rushil kalidas
#15 April 2014

def get_integer(x):
   a="Enter " +str(x)+":\n"
   n = input(a)
   while not n.isdigit ():
      n = input (a)
   x = eval (n)   
   return x


def calc_factorial(x):
   nkfactorial = 1
   for i in range (1, x+1):
      nkfactorial *= i
   
   return nkfactorial

