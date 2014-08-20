

N=eval(input("Enter the starting point N:\n"))                
M=eval(input("Enter the ending point M:\n"))                  
print("The palindromic primes are:")
palindrome=0
x=2
z=3 
a=5
b=7
c=11
y=0
for i in range(N,M+1):                                        
    palindrome=str(i)[::-1]                                 
    y=eval(str(i))
    
    if palindrome==str(i):                                    
            
            if y%x==0:
                break
            elif y%z==0:
                break
            elif y%a==0:
                break
            elif y%b==0:
                break
            elif y%c==0:
                break
            else:
                print(i)