numbers = "123456789"
def get_integer(n):
    num = input("Enter "+str(n)+":\n")
    while str(num)[0] not in numbers or eval(num) < 0:
        num = input("Enter "+str(n)+":\n")
    return eval(num)
def calc_factorial(num):
    nfactorial = 1
    for i in range (1, num+1):
        nfactorial *= i    
    return nfactorial
    