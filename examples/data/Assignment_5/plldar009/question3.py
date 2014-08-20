def get_integer(n): 
    integer = input("Enter " + n + ":\n")
    while not integer.isdigit ():
        integer = input("Enter " + n + ":\n")
    integer = eval(integer)
    return integer
      
def calc_factorial (n): 
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial   
