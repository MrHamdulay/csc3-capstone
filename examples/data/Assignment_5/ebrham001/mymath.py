'''Using combine.py to create a more readable and space efficient program
HAMZA EBRAHIM
17/04/14'''

# Assignment 5 - Question 3


# defining get_integer function

def get_integer(a):

# use while loop to ensure that input (n) provided is valid. ie. not negative or string   
   if a=="n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)

      return n
   
# use while loop to ensure that input (k) provided is valid. ie. not negative or string 

   if a=="k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)

      return k


# defining factorial function 
def calc_factorial(n):

# this is where the calculation of how many permutations there are takes place
   
      nfactorial = 1
      for i in range (1, (n)+1):
         nfactorial *= i

      return nfactorial       
   
# program ends