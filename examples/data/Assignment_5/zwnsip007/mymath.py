'''mymath programme
Siphesihle Zwane 
15-04-16'''
def get_integer(x):#creating get interger for Q3
   n = ''
   while not n.isdigit ():
      n = input ("Enter "+x+":\n")
   return int(n)
      
def calc_factorial(x): #creating calc_factorial for q3
   
   nfactorial = 1
   for i in range (1,x + 1):
      nfactorial *= i 
   return nfactorial
   
