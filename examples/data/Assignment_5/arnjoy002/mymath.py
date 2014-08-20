#Joy Arendse-Gorvalla
def get_integer(x): #defining a function
    print('Enter', x, end='')
    print(':')
    x = input()
    
    while not x.isdigit(): #loop
        print('Enter', x, end='')
        print(':')
        x = input()
    x = eval(x)
    return x

def calc_factorial(x): #defining new function
    fact=1
    for i in range(2,x+1): #loop 
        fact*=i
    return fact