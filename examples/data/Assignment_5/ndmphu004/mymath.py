#Phumelele Ndimande
#Assignment 5

def get_integer(x):
    value =0
    if x == 'n':
        n=input("Enter n:\n")
        while not n.isdigit():
            n=input("Enter n:\n")
        num=eval(n)
    elif x == 'k':
        k=input("Enter k:\n")
        while not k.isdigit():
            k=input("Enter k:\n")
        num=eval(k)
    return num
    
def calc_factorial(x):
    
    factorial=1
    
    for i in range(1, x+1):
        factorial = factorial*i
    return factorial
    