#MyMath
#Sofia Palmer
#15 April 2014

def get_integer(a):
      n = input ("Enter "+ a +":\n")
      while not n.isdigit() or eval(n) < 0:
            n = input ("Enter " + a +":\n") 
      n = eval (n)  
      return n 
def calc_factorial(a):
   afactorial = 1
   for i in range (1, a+1):
      afactorial *= i
   return afactorial

   
