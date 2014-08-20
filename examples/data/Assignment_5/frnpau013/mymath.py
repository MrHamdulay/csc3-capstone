def get_integer(s):
    ask_string = "Enter " + s + ":\n"
    n = input(ask_string)
    while not n.isdigit():
        n = input(ask_string)
    return int(n)

def calc_factorial(s):
    factorial = 1
    for i in range (1, s+1):
        factorial *= i    
    return factorial