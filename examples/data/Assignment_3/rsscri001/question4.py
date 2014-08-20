#Palindromic Primes between two inergers
import math
  
N=eval(input("Enter the starting point N: \n"))
M=eval(input("Enter the ending point M: \n")) 
print("The palindromic primes are:")
x=1
for i in range(N+1,M):
            
            trial_number=N+x
    
            trial_String=str(trial_number) #converting int into string
        
            if all(i%k!=0 for k in range(2,int(math.sqrt(i))+1)):#to check for prime numbers
                        
                        if(trial_String==trial_String[::-1]):
                                    
                                    print(trial_String)
                
            x=x+1




    
    
    
    
    