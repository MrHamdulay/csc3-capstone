""""assignment5
question3
15 april 2014,
Mphuthi Mamorena"""

def get_integer(x):
    y= input ("Enter x:\n".replace('x',x))#to make it print the parameter
    while not y.isdigit ():# to iterate while the parameter is not a number
        y = input("Enter x:\n".replace('x',x))
    x=y
    x = eval (x)#turning a parameter into int for calculations  
    return x

def calc_factorial(y):
    xfactorial=1
    for i in range (1, y+1):
        xfactorial*=i
    return xfactorial
        
        
