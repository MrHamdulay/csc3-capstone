def get_integer (x):
   print("Enter",x,end="")
   x1=input (":\n")
   while not x1.isdigit ():
      print("Enter",x,end="")
      x1= input (":\n")
   x1 = eval (x1)
   return x1
   
def calc_factorial (y):
   yfactorial = 1
   for i in range (1, y+1):
      yfactorial *= i
   return yfactorial