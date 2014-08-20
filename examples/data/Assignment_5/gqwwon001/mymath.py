# A programme to to refactor and reorganise combine.py
# Wongwa Giqwa
# 15 April 2014

# Function to get an integer
def get_integer(n):
    if n == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n") 
        n = eval(n)
        return n
          
    if n == "k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        return k    
   
    
# Funtion to calculate the factorial
def calc_factorial(n):
    fact=1
    for factor in range(1,n+1):
        fact=fact*(factor)
    return(fact)
       
   
        

       
