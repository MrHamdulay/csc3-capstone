def get_integer(x):
   n = input ("Enter "+x+":\n")
   while not n.isdigit ():
      n = input ("Enter "+x+":\n")
   n = eval (n) 
   return n 
   
   
def calc_factorial(x):
   
   fact = 1
   for i in range(2,x+1):
      fact*=i
      
   return fact
      
      
      