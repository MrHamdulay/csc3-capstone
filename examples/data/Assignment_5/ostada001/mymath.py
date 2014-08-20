#Adam Oosthuizen
#mymath
#17 April 2014
''' Import module for question 3 assignment 5'''


def get_integer(x): 
      z = input ("Enter "+(x)+":\n")
      while not z.isdigit ():
            z = input ("Enter "+(x)+":\n")      
      z = eval (z)

      return z

def calc_factorial(y):
      ykfactorial = 1  
      if type(y) == int:
            for i in range (1, y + 1):
                  ykfactorial *= i
      return ykfactorial