def get_integer(x):
    
    if x=='n':
        while not x.isdigit ():
            x=input('Enter n:\n')
        x=eval(x)
    elif x=='k':
        while not x.isdigit ():
            x=input('Enter k:\n')
        x=eval(x)
    return x
def calc_factorial(z):
    nfactorial = 1
    for i in range (1, int(z)+1):
        nfactorial *= i 
    return nfactorial
        
        