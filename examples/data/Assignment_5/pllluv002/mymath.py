def get_integer(x):
    y="Enter "+str(x)+":\n"
    n = input (y)
    while not n.isdigit ():
       n = input (y)
    x = eval (n)    
    return x


def calc_factorial(x):
    nkfactorial = 1
    for i in range (1, x+1):
       nkfactorial *= i 
       
    return nkfactorial
    
  
    
