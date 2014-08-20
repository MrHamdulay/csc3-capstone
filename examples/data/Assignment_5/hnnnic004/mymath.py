'''program for permutations
nicole henning
due 17 april'''

#create functions with the functions called
#use the code in combine to derive code for seperate fucntions

def get_integer(a):
   #for n
   if a == "n":
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      return int(n)
   
   #for k
   elif a == "k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      return int(k)
    

def calc_factorial (b):
   #for n and n-k
   factorial = 1
   for i in range (1, b+1):
      factorial *= i   
   return int(factorial)
   
      
      