#Creating function to calculate factorials
#Lauren de Bruyn
#14 April 2014

#get a number n or k from the user
def get_integer(n):
    if n=="n":   
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        return int(n)
    
    elif n=="k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        return int(k)

#calculating the factorial
def calc_factorial (c): 
    nfactorial = 1
    for i in range (1, c+1):
        nfactorial *= i
    return int(nfactorial)
    