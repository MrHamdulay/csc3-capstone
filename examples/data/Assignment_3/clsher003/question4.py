  
starting_point=eval(input("Enter the starting point N:\n"))
end_point=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
import math

#determine if the number is a prime
def prime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            return False
    if number == 2: 
            return True    
    elif number < 2:
            return False    
    return True
    
for i in range(starting_point+1,end_point):
    if prime(i)==True: # will only execute if number is a prime
        i=str(i)
        if i==i[::-1]: #determines if number is palindromic
            a=int(i)
            print(i)    
    
            
            
            


    
            
            
        
        
        
            
            
            
            

    
        
    
    
    



