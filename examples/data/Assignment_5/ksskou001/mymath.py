'''These functions are used to calculate the k-permutations of n items 
Kouame KOUASSI
12 april 2014'''

#function to get the variable n and k
def get_integer(x):
    if x == 'n' :
        x = input ('Enter n:\n')
    #repeat the above if input not digit or negative        
        while not x.isdigit ():
            x = input ('Enter n:\n')
    elif x == 'k':
        x = input ('Enter k:\n')
        while not x.isdigit ():
            x = input ('Enter k:\n')
    x = eval (x) 
    return x
    
#function to calculate the factorial of a number x    
def calc_factorial (x):
    xfactorial = 1
    for i in range (1, x+1):
        xfactorial *= i 
    return xfactorial