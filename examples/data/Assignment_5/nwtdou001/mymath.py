def get_integer(v):
    x = 'x'
    while not x.isdigit():
        x = input('Enter '+v+':\n')
    return eval(x)

def calc_factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact *= i
    return fact