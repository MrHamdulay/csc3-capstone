# Assignment 3 Question 4
#Name: Shaheen Karodia
#Student Number: KRDSHA003
#Date 2014-03-20

#Find all palindromic primes between two integers supplied as input (start and end points are excluded).

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
if N==1:
    print(2)     #2 although prime will lead not meet the condition of the loop
for i in range (N+1,M):
    
    i=str(i)  # convert number to a string 
    if i==i[::-1]: #Check forward vs Backawrd
        i=int(i)       #convert it back into an integer
        j=2           #Initialise j outside of while loop so it starts at 2 every time 
        
        while True:
            if i%j==0:   
                break
            
            else:
                j=j+1
                if j==i:
                    print(i)
                    break        
        
        
        

     
    
    


        
        
        
        
        

 

