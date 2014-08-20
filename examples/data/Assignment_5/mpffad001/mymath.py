#a program to reuse/adapt the code in the complete program 
#fadzai mupfunya
#13 April 2014

def get_integer(num):
    n = input ("Enter "+num+":\n")       
    while not n.isdigit ():
        n = input ("Enter "+num+":\n")    
    return eval(n)

def calc_factorial(num2):
    num2factorial = 1
    for i in range (1, num2+1):
        num2factorial *= i 
    return num2factorial