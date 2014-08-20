"""
Prashanth Sridharan
SRDPRA001
Assignment 5
Question 3; mymath
"""
def get_integer(string):
     n = input ("Enter "+string+":\n")
     while not n.isdigit ():
          n = input ("Enter "+string+":\n")
     n = eval (n)
     return n
def calc_factorial(i):
     if i <1:   #this is the base case; or the terminator step to prevent an infinite loop
          return 1
     else:
          nfactorial = i * calc_factorial( i - 1 )  # the part the function calls itself and loops through      recursion 
          #print(str(n) + '! = ' + str(nfactorial))
          return nfactorial
'''def get_integer (s):
   n = input ("Enter "+s+":\n")
   while not n.isdigit ():
      n = input ("Enter "+s+":\n")
   n = eval (n)
   return n
   
def calc_factorial (n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial   '''