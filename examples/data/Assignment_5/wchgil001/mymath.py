#integer factorial
#Gillian Wachira
#19 april 2014

def get_integer (n):
    p=input("Enter "+n+":\n")
    while not p.isdigit ():
        p=input("Enter "+n+":\n")
    p=eval(p)
    return p
def calc_factorial (n):
    factorial=1
    for i in range(1, n+1):
        factorial *=i
    return factorial