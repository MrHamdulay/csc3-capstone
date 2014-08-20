"""calculate number of k-permutations of n items
Elizabeth Cilliers
14/04/2014"""

def get_integer(integer):
   
   if integer=="n": #if integer is n then as user to enter n and then convert it into an int
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return n
   
   if integer=="k": #if integer is k then as user to enter k and then convert it into an int
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)      
      return k

def calc_factorial(value): #calculate the factorial of the value for either n or n-k 
   
   factorial = 1
   for i in range (1, value+1):
      factorial *= i
   return factorial
   