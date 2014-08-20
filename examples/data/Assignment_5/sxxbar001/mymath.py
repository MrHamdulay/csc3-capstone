#Assignment 5
#Question 3
#Barry Su
#15 April 2014

#create the function to get integer
def get_integer(x):
   if x == "n":
      global n
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return n
           
   else:
      global k
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k
   
#create function to give the factorial
def calc_factorial(x):
   nfactorial=1
   for i in range(1,x+1):
      nfactorial*=i
     
   return nfactorial

    
