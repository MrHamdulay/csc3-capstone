import math
start=eval(input("Enter the starting point N:\n"))
stop=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(start+1,stop):
    number=str(i)
    reverse=(str(i)[::-1])
    if number == reverse:
        x=False
        j=2
        while j<i:
            if i%j==0:
                x=False
                break
            
            else:
                x=True
            j+=1
        else:
            x=True
        if x==True:
            print(i)
    
            
        
            
        
                
         
    
    
    
    