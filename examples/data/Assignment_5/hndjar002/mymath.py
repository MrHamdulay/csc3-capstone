'''Using combine.py to create a more readable and space efficient program
17/04/14'''
# defining get_integer function
def get_integer(a):
         n = input ("Enter n:\n")
         while not n.isdigit ():
            n = input ("Enter n:\n")
         n = eval (n)
         return n
# use while loop to check if k is valid
      if a=="k":
         while not k.isdigit ():
            k = input ("Enter k:\n")

# defining factorial function 
def calc_factorial(n):
      nfactorial = 1
      for i in range (1, (n)+1):
         nfactorial *= i
      return nfactorial       