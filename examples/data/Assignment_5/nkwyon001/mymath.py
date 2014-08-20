"""finding k and n from user
Yondela Nkwali
16 April 2014"""

def get_integer(r):   
      n = input ("Enter "+r+":\n")
      while not n.isdigit ():
            n = input ("Enter "+r+":\n")
      n = eval (n)
      return n


#getting the factorial of r
def calc_factorial(r):
      nfactorial = 1
      for i in range (1, r+1):
            nfactorial *= i
      return nfactorial
