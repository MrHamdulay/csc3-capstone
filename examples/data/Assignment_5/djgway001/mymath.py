#calculate number of k-permutations of n items
#wayne de jager
#15 april 2014


def get_integer(n):
    s=input("Enter "+n+":\n")
    while not s.isdigit():
        s=input("Enter "+n+":\n")
    n=eval(s)
    return n

def calc_factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial