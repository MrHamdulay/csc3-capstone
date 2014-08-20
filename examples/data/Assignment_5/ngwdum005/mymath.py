"""Dumisani Ngwenza
NGWDUM005
13/04/2014
Assignment 5 Question 3"""

#gets a variable and stores the value
def get_integer(n):
    if n == 'n':
        
        while not n.isdigit ():
                n = input ("Enter n:\n")
    if n == 'k':
        while not n.isdigit():
                n = input ("Enter k:\n")
    n = eval (n) 
    return n

#calculates the factorial of the stored number
def calc_factorial(x):
    a = x
    xfactorial = 1
    for i in range (1, a+1):
        xfactorial *= i
    return xfactorial 

if __name__=='__main__':
    print(get_integer("b"))
    print (get_integer("k"))