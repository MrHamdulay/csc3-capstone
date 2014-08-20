# Question 1
# Name: Khanyisile Morudu
# Student Number: mrdkha001
# Date: 10/04/2014


# Getting the integer
def get_integer(string):
   num = 0
   #integer can either be the k part or n part
   if string == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      num = eval (n) 
   elif string == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      num = eval (k)
   return num

#calculating the factorial
def calc_factorial(num):
   nfactorial = 1
   for i in range (1, num+1):
      nfactorial *= i   
   return nfactorial