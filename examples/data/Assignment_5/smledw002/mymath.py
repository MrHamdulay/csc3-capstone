# calculate number of k-permutations of n items
# Edwin Samuels
# Student number Smledw002
# 16 april 2014
def get_integer(n):#To ensure a intager is received from the user
    x=n # in order to maintain the original variable name of n for each iteration
    while not x.isdigit():
        x = input('Enter '+n+':\n')
        if x.isdigit():
            x = eval(x)
            break  #breaks loop to prevent syntax error int.isdigit()
    return x

   
def calc_factorial(n):  #determines the factorial of n
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
