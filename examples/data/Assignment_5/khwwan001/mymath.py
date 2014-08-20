'''program to calculate the number of permutations when given integer n and integer k
Wandile Khowa
16-04-2014
'''

def get_integer(p): #create a function called get_integer which checks if the input is a digit or not
    if p == 'n':
        n = input ("Enter n:\n")
        while not n.isdigit (): #while inout is not digit, keep on asking for more inout until correct input is entered
            n = input ("Enter n:\n")
        return eval(n)    
        
    else:
        k = input ("Enter k:\n") #works as the same as above
        while not k.isdigit ():
            k = input ("Enter k:\n")
        return eval(k)   
        
def calc_factorial(b): #calculates the value of the factorial of b
    fact = 1
    for i in range (1, b+1):
        fact *= i
    return fact #returns the computed value of b
    

    
    
    

        
         
            
        
    
    
    