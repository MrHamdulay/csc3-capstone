def get_integer():
    n=eval(input("Enter n:\n"))
    k=eval(input("Enter k:\n"))
           
get_integer()

def calc_factorial(n):
    
    n= get_integer(n)
    nfactorial=1
    while n>0:
        nfactorial=nfactorial*n
        n=n-1
    return(nfactorial)

calc_factorial()