def get_integer(var):
   x = input ("Enter " +var+ ":\n")
   while not x.isdigit ():
      x = input ("Enter " +var+ ":\n")
   return eval (x)      

def calc_factorial(var):
   factorial = 1
   for i in range (1, var+1):
      factorial *= i
   return factorial

