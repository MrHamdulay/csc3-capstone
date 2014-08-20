def get_integer(let):
   if let == "n":
      a = input ("Enter n:\n")  
      while not a.isdigit():
         a = input("Enter n:\n")
      a = eval(a)
   elif let == "k": 
      a = input ("Enter k:\n") 
      while not a.isdigit():
         a = input("Enter k:\n")
      a = eval(a)
   return a

def calc_factorial(a):
   nfactorial = 1
   for i in range (1, a+1):
      nfactorial *= i
   return nfactorial
