# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

#Modified to mymath.py by Sabir Buxsoo.
#Date Modified: 17/04/2014

#Functions grabs the parameter and assigns the value to n and k respectively.
def get_integer(a):
   if(a == "n"):
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return(n)
   
   if(a == "k"):
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)   
      return(k)


#Function which grabs the parameter and calculates the factorial.
def calc_factorial(b):
   factorial = 1
   for i in range (1, b+1):
      factorial *= i
   return (factorial)
   
