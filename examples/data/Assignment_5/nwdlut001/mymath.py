def calc_factorial(y):
    xfactorial=1
    for i in range (1, y+1):
        xfactorial*=i
    return xfactorial
        

def get_integer(x):
    y= input ("Enter x:\n".replace('x',x))
    while not y.isdigit ():
        y = input("Enter x:\n".replace('x',x))
    x=y
    x = eval (x)  
    return x

