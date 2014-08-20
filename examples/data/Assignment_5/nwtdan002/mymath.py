"""Two functions used to find k-permutations for n items
By Daniel Newton
13/04/14"""

def get_integer(n):
    
    #Prompting the user to enter a value for whatever string chosen.
    print("Enter ",n,":",sep='')
    num=input()
    
    while not num.isdigit ():   #Used to check is the number entered is a digit
        print("Enter ",n,":",sep='')
        num=input()
        
    num=eval(num)  
    return num


def calc_factorial(fact): #Calculating the value of a value factorial (e.g. 5! = 5*4*3*2*1)
    
    nfactorial=1
    for i in range (1, fact+1): #Calculating 'fact!'
        nfactorial *= i
        
    return nfactorial