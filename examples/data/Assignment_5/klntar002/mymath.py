def get_integer(p):
    el = input ('Enter '+ str(p)+':\n')
    while not el.isdigit ():
        el = input ('Enter '+ str(p)+':\n')
    el = eval (el)   
    return el
 
    
def calc_factorial(yy):
    factorial = 1
    for i in range (1, yy+1):
        factorial *= i  
    return factorial
    