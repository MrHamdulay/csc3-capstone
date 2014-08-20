def get_integer(option):
    if option == 'n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)           
        return n
    else:
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        return k
def calc_factorial(x):
    factorial = 1
    for i in range (1, x+1):
        factorial *= i
    return factorial   

        