'''Using combine.py to create a more readable and space efficient programJaren HendricksAssignment 5  Question 3
17/04/14'''
# defining get_integer function
def get_integer(a):      if a=="n":
         n = input ("Enter n:\n")
         while not n.isdigit ():
            n = input ("Enter n:\n")
         n = eval (n)
         return n
# use while loop to check if k is valid
      if a=="k":         k = input ("Enter k:\n")
         while not k.isdigit ():
            k = input ("Enter k:\n")         k = eval (k)         return k

# defining factorial function 
def calc_factorial(n):
      nfactorial = 1
      for i in range (1, (n)+1):
         nfactorial *= i
      return nfactorial       