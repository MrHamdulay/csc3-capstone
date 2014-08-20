"""Alternative to combine
Micaela Narasmulu
16 April 2014 """

def get_integer(x): #returns the integer value of parametered string
   m = input ("Enter "+x+":\n")
   while not m.isdigit ():
      m = input("Enter "+x+":\n")
   m=eval(m)
   return m


def calc_factorial(x): #returns the factorial of parametered integer
   fact=1
   for i in range(2,x+1):
      fact*=i
   return fact