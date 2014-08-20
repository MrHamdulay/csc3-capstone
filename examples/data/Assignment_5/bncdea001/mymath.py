# My Math
#Functions to tidy things up
#Dean Bunce
#14 April 2014
def get_integer(x):
        
        
        #Print parameter when getting input
        print_x=str(x)
        
        #Set run to false to facilitate for loop
        run=False
        
        #Create a while looop
        while run == False:
                x=input("Enter " + print_x + ": \n")
                
                #Don't process negatives or things that aren't digits
                if not x.isdigit() or eval(x)<=0:
                        continue
                
                #If a number is input stop asking for input
                if run==True:
                        break
                
                return eval(x)
                
        

        
    
        
    
    
    
        
    
def calc_factorial(x):
    nkfactorial = 1
    for i in range (1, x+1):
        nkfactorial *= i   
    return nkfactorial
