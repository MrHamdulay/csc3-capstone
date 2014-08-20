start = eval(input("Enter the starting point N:\n"))
end = eval(input ("Enter the ending point M:\n"))
prime = True
import math
print("The palindromic primes are:")
for i in range (start+1,end):
    k= str(i)
    if k == k[::-1]:
        prime = True
        for j in range(2,round(math.sqrt(i))+1):
            
            if i%j==0:
                prime = False

        if prime:
            print(i)

                
            
                
        
        
            
            
        
