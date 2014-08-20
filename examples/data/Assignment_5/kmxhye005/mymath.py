# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

def get_integer(x):
    if x == "n":
        while not x.isdigit():
            x = input ("Enter n: \n")
        x = eval(x)
        return x
    
    if x == "k":
        while not x.isdigit():
            x = input ("Enter k: \n")
        x = eval (x)
        return x
        
def calc_factorial(n):
    factorial = 1
    for i in range (1, n+1):
        factorial *= i
    return factorial


