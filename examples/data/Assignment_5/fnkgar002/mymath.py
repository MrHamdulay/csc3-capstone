#Calculating number of perumatations of a number of items
#gary Finkelstein
#15 April 2014


#method that recieves a value and is used to return an integer using validation to ensure the return variable is a number 
def get_integer(strvalue):
   
   value = strvalue.lower()
   if (value == "n"):
      n = input ("Enter n:\n")
      while n.isdigit() == False:
         n = input ("Enter n:\n")
      n = eval (n) 
      return n
   
   elif(value != "n"):
      k = input ("Enter k:\n")
      while k.isdigit() == False:
         k = input ("Enter k:\n")
      k = eval (k)
      return (k)

#method that recieves a value and is used to calculate the numbers factorial
def calc_factorial(value):
   fact = 1
   num = value +1
   for i in range (1, num):
      fact = fact * i
   return fact