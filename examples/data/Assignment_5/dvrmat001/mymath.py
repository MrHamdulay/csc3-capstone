def get_integer(x):
    if x == "n":
        x = input ("Enter n: \n")
        while not x.isdigit():
            x = input ("Enter n: \n")
        x = eval(x)
        return x
    if x=="k":
        x = input ("Enter k: \n")
        while not x.isdigit():
            x = input ("Enter k: \n")
        x = eval (x)
        return x
        
def calc_factorial(x):
    nfactorial = 1
    for i in range (1, x+1):
        nfactorial *= i
    return nfactorial
