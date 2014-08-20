#function used in calculating the number of k-permutations of n items
#Conor O'Sullivan
#15/04/2014

#Asks user to enter integers n & k
def get_integer (x):
    integer = input("Enter " + x +":\n")
    valid = False
    
    while valid==False:
        
        if integer.isdigit():
            integer = eval(integer)
            if integer >=0:
                return integer
                
        integer = input("Enter " + x +":\n")
        
    return integer

#calculates factorials of n & k
def calc_factorial(x):
    factorial = 1
    for i in range (1, x+1):
        factorial *= i   
    return factorial