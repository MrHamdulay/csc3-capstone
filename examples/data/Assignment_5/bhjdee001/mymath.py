#deepak
#q3 
def get_integer(z): #returns the int val 
   a = input ("Enter "+z+":\n")
   while not a.isdigit ():
      a = input("Enter "+z+":\n")
   a=eval(a)
   return a


def calc_factorial(a): #returns the factorial 
   f=1
   for i in range(2,a+1):
      f*=i
   return f