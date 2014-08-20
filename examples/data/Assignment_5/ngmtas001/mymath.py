#NGMTAS001
#Question3

def get_integer(num):
    if num =='n':
        global n
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)   
        return n
    elif num == 'k':
        global k
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)   
        return k
    
def calc_factorial(num):
    if (num == n):
        nfactorial = 1
        for i in range (1, num+1):
            nfactorial *= i
        return nfactorial
    else:
        nkfactorial = 1
        for i in range (1, n-k+1):
            nkfactorial *= i        
        return nkfactorial