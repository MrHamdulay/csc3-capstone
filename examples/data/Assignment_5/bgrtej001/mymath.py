#Assignment 5, Question 3
#My Math
#Tejasvin Bagirathi BGRTEJ001
#2014-04-17

#Define function get_integer()
def get_integer(x):
    prompt = ("Enter " + x + ":\n")
    x = input(prompt)
    while not x.isdigit ():
        x = input(prompt)
    x = eval(x)
    return x

#Define function calc_factorial()
def calc_factorial (y):
    nfactorial = 1
    for i in range (1, y+1):
        nfactorial *= i    
    return nfactorial
