def get_integer(option):
    if(option == "n"):
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        return eval (n)
    if(option == "k"):
            n = input ("Enter k:\n")
            while not n.isdigit ():
                n = input ("Enter k:\n")
            return eval (n)    

def calc_factorial (n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial