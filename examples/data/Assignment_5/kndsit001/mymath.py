"""Program to Determine Factorial
Sithasibanzi Kondleka
16 April 2014"""

def get_integer(z):
    x = "Enter "+ z +":\n"
    z = input(x)
    while not z.isdigit ():
        z = input(x)
    z = eval (z)
    return z
def calc_factorial(z):
    factorial = 1
    for i in range (1, z+1):
        factorial *= i
    return factorial