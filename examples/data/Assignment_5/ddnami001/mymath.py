#Amitha Doodnath
#DDNAMI001
#14/04/2014
#Alternate to combine.py

def get_integer(x): #returns the integer value of parametered string
   r = input ("Enter "+x+":\n")
   while not r.isdigit ():
      r = input("Enter "+x+":\n")
   r=eval(r)
   return r


def calc_factorial(x): #returns the factorial of parametered integer
   fact=1
   for i in range(2,x+1):
      fact*=i
   return fact