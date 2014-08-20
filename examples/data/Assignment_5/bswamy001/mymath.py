"""Amy Bosworth, mymath,  question 3,  assignment 5"""

#function to get integer n or k
def get_integer(choice):
    if choice=='n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n) 
        return n
    
    elif choice=='k':
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)    
        return k 

def calc_factorial(x):
    y = 1
    for i in range (1, x+1):
        y *= i 
    return y
    
    
    


