def get_integer(x):
    integer=input("Enter "+x+":\n")
    while not integer.isdigit():
        integer=input("Enter "+x+":\n")
    integer=eval(integer)
    return integer

def calc_factorial(y):
    nfactorial=1
    for i in range(1,y+1):
        nfactorial=nfactorial*i
    return nfactorial    