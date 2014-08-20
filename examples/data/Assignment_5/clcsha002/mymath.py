"""mymath alterations
shannonclacey
15 april 2014"""

#in this program i have created two functions which I saw were used in the question three which was provided

#I have first looked at the function to calculate the factorial of the given number
def calc_factorial(x):
   factorial = 1
   for i in range (1, x+1):
      factorial *= i
   return factorial 

# I have now looked at the function to get an integer and merely slightly shortened  the function. this function converts a given input to an integer if it is interpreted as a string
def get_integer(a):
   if a == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n) 
      return n
   else:
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return (k)
