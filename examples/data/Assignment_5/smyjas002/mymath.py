def get_integer(qType):
   if qType == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      result = eval (n)   
   elif qType == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      result = eval (k)
   return result
   
def calc_factorial (n):
   nfactorial = 1
   for i in range (1, n+1):
      nfactorial *= i
   return nfactorial
