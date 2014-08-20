def get_integer(n):
    x = input ("Enter" + " " + n + ":\n")
    while not x.isdigit (): 
        x = input ("Enter" + " " + n + ":\n")
    y = eval (x)   
    return(y)
def calc_factorial(num): 
    factorial = 1  
    for i in range (1, num+1): 
        factorial *= i 
    return (factorial)  
   
    