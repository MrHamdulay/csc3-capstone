#glnrus002
#question3
#16 April
#Does calculations for question 3
def get_integer(l):#get user input
   lm=input("Enter "+ l+":")
   print()
   while not lm.isdigit ():
      lm=input("Enter "+ l+":")
      print()#otherwise words next to each other
   lm=eval(lm)
   return lm   

def calc_factorial(n):#final answer
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial