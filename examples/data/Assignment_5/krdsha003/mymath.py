
"""Assignment 5 Question 3 Module my math
defining input function and factorial calculator functions
Shaheen Karodia
KRDSHA003
2014-04-16"""




def get_integer(x):
    """gets input from user for n and k"""
    
    if x=="n":                   #get value for n
        n = input ("Enter n:\n") 
        while not n.isdigit ():   #loop runs till user inputs a number
            n = input ("Enter n:\n")
        return eval (n)           
    
    else:
        k = input ("Enter k:\n")  #get value for k
        while not k.isdigit ():
            k = input ("Enter k:\n")
        return eval (k)        
        
        
          
        
   
    
  
def calc_factorial(x):
    """"function to calculate the factorial of a number"""
    
    factorial=1           
    for i in range(1,x+1):
        factorial *= i
    return factorial
        

