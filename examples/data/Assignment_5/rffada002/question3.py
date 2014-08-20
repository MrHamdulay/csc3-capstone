global n,k,x,z

def get_integern ():
      global n
      n = input ("Enter n:\n")
      while not n.isdigit ():
            n = input ("Enter n:\n")
      n = eval (n)
      

def get_integernk():
      global k
      k = input ("Enter k:\n")
      while not k.isdigit ():
            k = input ("Enter k:\n")
      k = eval (k)
      
   

def calc_factorialn (n):
      global x
      nfactorial = 1
      for i in range (1, n+1):
            nfactorial *= i
      x = nfactorial
      

def calc_factorialnk (y):
      global z
      nkfactorial = 1
      for i in range (1, y+1):
            nkfactorial *= i
      z = nkfactorial
      


get_integern ()
get_integernk()
y = n-k
calc_factorialn (n)
calc_factorialnk (y)
print("Number of permutations:", x//z)