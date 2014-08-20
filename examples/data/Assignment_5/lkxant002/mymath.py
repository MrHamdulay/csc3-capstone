def get_integer(x):
   print("Enter ",x,":",sep="")
   n = input ()
   while not n.isdigit ():
      print("Enter ",x,":",sep="")
      n = input ()
   n = eval (n)  
   return n

def calc_factorial(n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial

