'''Program which calculates the number of k-permutations of n items
Sandile Mahlangu
14 April 2014'''
def get_integer (i):
    '''This function gets a value from the user'''
    if i=='n': #Gets the value for n
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        c=n
    elif i=='k':#Gets the value for k
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        c=k
    return c
def calc_factorial (n_0r_n_k):
    '''Calculates the factorials of n and n-k'''
    factorial_value = 1
    for i in range (1, n_0r_n_k+1):
        factorial_value *= i  
    return factorial_value 