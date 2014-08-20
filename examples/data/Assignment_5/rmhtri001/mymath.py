def get_integer(choice):
    if choice == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)           
        return n
    elif choice == "k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)           
        return k

def calc_factorial(variable):
    z = 1
    for i in range (1, variable+1):
        z *= i  
        
    return z
    