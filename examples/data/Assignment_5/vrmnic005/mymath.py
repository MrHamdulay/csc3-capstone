#VRMNIC005
#assignment 5, question 3

def get_integer(name):
    """Prompts user for an integer input"""
    number = input("Enter "+name+":\n")
    while not number.isdigit(): #will prompt again if an integer wasnt provided
        number = input("Enter "+name+":\n")
    number = int(number)
    return number
    
def calc_factorial(n):
    """Calculates the factorial"""
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
