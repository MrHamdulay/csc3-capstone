n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

if n==0 or n==1:
        print(2) 
        
n=n+1

for i in range(n,m,1):
        n=str(n)
        rev=n[::-1]
        n=eval(n)
                     
        if rev==str(n):
                for i in range(2,n):
                        if n%i ==0 :
                                break
                        elif i<(n-1):
                                continue  
                        else:
                                print(n)
                                break
        n=n+1
                                
                     
                                
        
                
        