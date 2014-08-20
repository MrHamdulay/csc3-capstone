def get_integer(str):
    s = input("Enter "+str+":\n")
    while not s.isdigit():
        s = input("Enter "+str+":\n")
    return eval(s)

def calc_factorial(int):
    factorial = 1
    for i in range (1, int+1):
        factorial *= i    
    return factorial
    