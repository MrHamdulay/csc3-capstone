def calc_factorial (x):  
   nfactorial = 1
   for i in range (1, int(x)+1):
      nfactorial *= i
   return nfactorial

def calc_factorial (x):
   nkfactorial = 1
   for i in range (1,int(x) +1):
      nkfactorial *= i
   return nkfactorial

def get_integer(c):
   input_var = str("Enter "+str(c)+":\n")
   n = input (input_var)
   while not n.isdigit ():
      n = input (input_var)
   global x
   x = eval (n)   
   return x


