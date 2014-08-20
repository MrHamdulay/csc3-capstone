''' Assignment 5 Question 3
Matshepo Malatji
15 April 2014'''

def get_integer(s):
#ask the user to input until the value is a number  
    n = s
    while not n.isdigit ():
        n = input ("Enter " +s +":\n") 
    return eval(n)

def calc_factorial (i):
#calculate the factorial of the given number
    int(i)
    factorial = 1
    for k in range(1, i+1):
        factorial *= k
    return factorial