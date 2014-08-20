"""2 functions which calculate given input when called
Dudley Mutero
13-4-14"""

def get_integer(text):
   #prompts user to input the 1st and second values of their permutations
   print("Enter ",text,":",sep="")
   val=input()
   while not val.isdigit ():
      print ("Enter ",text,":", sep="")
      val=input()
   return eval (val)

   
def calc_factorial(text2):
   #calculates the factorial of given input
   nfactorial = 1
   for i in range (1, text2+1):
      nfactorial *= i   
   return nfactorial
