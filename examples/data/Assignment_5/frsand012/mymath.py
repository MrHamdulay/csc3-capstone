
def get_integer (x):
    integer = x
    while not x.isdigit():
        x = input("Enter " + integer + ":\n")
    y = eval(x)
    
    return y
    
def calc_factorial (y):
    
    factorial = 1
    for i in range(1, y + 1):
        factorial *= i
            
    return factorial