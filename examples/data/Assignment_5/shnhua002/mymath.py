"""MyMath module
Charlie Shang
Assignment 5 Num3 15 April 2014"""

def get_integer(Num):
  
  if Num == "n": #for 'n items'
    
    n = input ("Enter n:\n")
   
    while not n.isdigit (): #repeat input until number is valid
      n = input ("Enter n:\n")
    n = eval (n)
    
    return n
  
  elif Num == "k": #for 'k permutations'
    k = input ("Enter k:\n")
    
    while not k.isdigit ():
      k = input ("Enter k:\n")
    k = eval (k)
    
    return k
  
def calc_factorial(val):
  f = 1 #instantiates the variable and begins calculation at 1
  for i in range (2, val+1): #begins at 2 because 1 x 1 = 1, saves wasted processing time
    f *= i
  return f