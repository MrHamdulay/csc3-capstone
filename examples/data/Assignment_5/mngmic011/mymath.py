#mymath
#Micaela Menegaldo

def get_integer(a):
    k=input("Enter "+a+":\n")
    while not k.isdigit():
        k=input("Enter "+a+":\n")
    k=eval(k)
    return k
    
def calc_factorial(h):
    #eval(h)
    nfactorial=1
    for i in range(1,h+1):
        nfactorial*=i
    return nfactorial

    