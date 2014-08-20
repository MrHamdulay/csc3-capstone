def get_integer(x):
   num = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "100"}
   if x == "n":
      x = input("Enter n:\n")
      if x not in num:
         x = input("Enter n:\n")
         if x not in num:
            x = input("Enter n:\n")
            x = int(x)
      elif x in num:
         x = int(x)   
   elif x == "k":
      x = input("Enter k:\n")
      if x not in num:
         x = input ("Enter k:\n")
         if x not in num:
            x = input ("Enter k:\n")
            x = int(x)
      else:
         x = int(x)
   return x


# This code was taken from Bhavana Harrilal's programme
def calc_factorial(y):
   nfactorial = 1
   for i in range (1, y+1):
      nfactorial *= i
   return nfactorial



