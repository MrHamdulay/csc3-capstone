'''My Math recreate combine.py
Michael Sanne
2014/04/15'''

#Return integer value 
def get_integer (n):
   number = input ("Enter " + n + ":\n")
   while not number.isdigit ():
      number = input ("Enter " + n + ":\n")
   number = eval (number)
   return number

#Calculate factorial of input integer
def calc_factorial (number):
   factorial = 1
   for i in range (1, number+1):
      factorial *= i
   return factorial