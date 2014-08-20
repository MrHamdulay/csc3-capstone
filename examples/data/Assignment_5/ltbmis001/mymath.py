def get_integer(n):
   n = input (("Enter "+n+":\n"))
   while not n.isdigit ():
      n = input (("Enter "+n+":\n"))
   n = eval (n)
   return(n)

def calc_factorial(n):
   factorial = 1
   for i in range (1, n+1):
      factorial *= i
   return(factorial)
      
