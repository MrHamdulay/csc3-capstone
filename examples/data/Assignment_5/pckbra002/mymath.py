# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014
#edited by Brandon Pickup 2014/04/14


n = input ("Enter n:\n")#asks the user for the value to n
while not n.isdigit():#continues asking the user for an n value until a digit is provided
   n = input ("Enter n:\n")
n = eval(n)#converts n to a number after checking that it is a number with the isdigit() function
k = input ("Enter k:\n")#same as above for the n variable
while not k.isdigit():
   k = input ("Enter k:\n")
k = eval(k)
def get_integer (x):#definition to return an integer
   if x=="n":#if the parameter provided is n, n is returned, else k is returned    
      return n
   else:     
      return k

def calc_factorial(x):#calculates the factorial value by running a loop from 1 to the value provided in the parameter
   nfactorial = 1
   for i in range (1, x+1):
      nfactorial *= i  
   return nfactorial


