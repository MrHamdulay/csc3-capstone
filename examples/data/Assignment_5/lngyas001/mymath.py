""" iproved combine program
yasha longstaff
15 bapril 2014"""

def get_integer(x):
   print("Enter",x,end = '')
   print(":")
   p = input ()
   while not p.isdigit ():
      print("Enter",x,end = '')
      print(":")
      p = input()
   return int(p)

def calc_factorial(y):
   nfactorial = 1
   for i in range (1, y+1):
      nfactorial *= i
      #nfactorial = eval(nfactorial)
   return nfactorial
   
