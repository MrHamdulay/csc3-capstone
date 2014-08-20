# calculate number of k-permutations of n items
# emiel zyde 
# 12 april 2014

def get_integer(integer):
   print("Enter ", integer,":", sep="")
   n = input ("")  
   while not n.isdigit ():
      print("Enter ", integer,":", sep="")
      n = input ("")        
   n = eval (n) 
   return n
   
def calc_factorial(x):
   xfactorial = 1
   for i in range (1, x+1):
      xfactorial *= i
   return xfactorial
      


