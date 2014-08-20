def get_integer(n):
    q=n=input("Enter n:\n")
    while not n.isdigit():
        n=input("Enter n:\n")
    q=eval(n)
    return q

def calc_factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial

def mymath():
    get_integer(n)
    calc_factorial(n)