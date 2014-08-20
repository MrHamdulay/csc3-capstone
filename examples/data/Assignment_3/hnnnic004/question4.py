N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
N+=1
    
print("The palindromic primes are:")      
for i in range (N,M):
        y=True
        a=str(i)
        if a==a[::-1]:
                if i>=2:     
                    for N in range (2,i):
                        if (i%N==0):
                            y=False
                            break
                    if y:
                        print(i)
                    
