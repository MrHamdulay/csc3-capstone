def get_integer(st):
    if st=='n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)   
        return n
        
    if st=='k':
        k = input('Enter k:\n')
        while not k.isdigit():
            k = input('Enter k:\n')
        k=eval(k)
        return k

def calc_factorial(integer):
    nfactorial = 1
    for i in range (1, integer+1):
        nfactorial *= i
    return nfactorial

