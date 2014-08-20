#n = input ("Enter n:\n")
#while not n.isdigit ():
   #n = input ("Enter n:\n")
#n = eval (n)   

'''k = input ("Enter k:\n")
while not k.isdigit ():
   k = input ("Enter k:\n")
k = eval (k)'''


def get_integer(a):
   if a == "n":
      n =(input ("Enter n:\n"))
      while not n.isdigit ():
         n =input ("Enter n:\n")
      n=eval(n) 
      return n
   if a == "k": 
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k
#get_integer()
   




'''nfactorial = 1
for i in range (1, n+1):
   nfactorial *= i

nkfactorial = 1
for i in range (1, n-k+1):
   nkfactorial *= i'''
   
def calc_factorial(a):
   nfactorial = 1
   for i in range (1, a+1):
      nfactorial *= i  
      
      #nkfactorial = 1
      #for i in range (1, n-k+1):
         #nkfactorial *= i
   return  nfactorial 

   
   

   