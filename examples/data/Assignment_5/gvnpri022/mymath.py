"""question 3- assignment 5
prinesan govender
14 april 2014"""
def get_integer(a): #capture input
   command="Enter "+a+":\n"
   a = input (command)
   while not a.isdigit ():
      a= input (command)
   a = eval (a)
   
  
   return a 





   

def calc_factorial(x): #calculate the factorial
   nfactorial = 1
   for i in range (1, x+1):
      nfactorial *= i   
   
   return nfactorial