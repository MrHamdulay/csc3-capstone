N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

count = N+1
while(count < M):
    if(str(count) == str(count)[::-1] and count % 1 == 0):
        factors = 0       
        for i in range(count):
            if(count % (i+1) == 0):
                factors += 1
        
        if (factors == 2):
            print(count)
    count = count +1        
        
        
        