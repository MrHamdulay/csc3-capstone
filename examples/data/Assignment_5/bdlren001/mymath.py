# calculate number of k-permutations of n items
# Budeli Rendani 
# BDLREN001
# 10 april 2014

def get_integer(integer): # Defining function for entering enter the input
   if integer=="n":
      n = input ("Enter n:\n")
      while not n.isdigit (): # If n that is entered is not a digit,ask for input again
         n = input ("Enter n:\n")
      n = eval (n) # convert input from an string to an digit
      return n
   
   if integer=="k":
      k = input ("Enter k:\n")
      while not k.isdigit (): # If n that is entered is not a digit,ask for input again
         k = input ("Enter k:\n")
      k = eval (k)# convert input from an string to an digit
      return k

def calc_factorial(n): #defining the function for calculating the factorial
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial


