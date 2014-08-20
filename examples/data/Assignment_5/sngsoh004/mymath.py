#SNGSOH004
#Assignment 5
#Question3


def get_integer(string):
    number = input("Enter "+string+":\n")
    while not number.isdigit (): #(While the input was not an integer value)
        number = input("Enter "+string+":\n") 
    number = eval (number) 
    return number

def calc_factorial(num):
    nfactorial = 1
    for i in range (1, num+1):
        nfactorial *= i    #Incrementing by multiplying
    return nfactorial