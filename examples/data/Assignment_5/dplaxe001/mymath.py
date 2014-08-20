#Axel du Plessis 14/04/2014

#Function to calculate the factorial of a value (n)
def calc_factorial(n):
    nFactorial = 1
    for i in range(1,n+1):
        nFactorial *= i
    return nFactorial

#Function to get the values of n and k
def get_integer(num):
    if num == "n":
        n = input("Enter n:\n")
        while n.isdigit() == False:
            n = input("Enter n:\n")
        n = eval(n)
        return n
        
    elif num == "k":
        k = input("Enter k:\n")
        while k.isdigit() == False:
            k = input("Enter k:\n")
        k = eval(k)
        return k