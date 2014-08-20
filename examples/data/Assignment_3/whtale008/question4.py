n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(n+1,m):
    if str(i) == str(i)[::-1]:
        p = 0
        for x in range(i):
            if i%(x+1) == 0:
                p = p+1
        
        if(p==2):
            print(str(i))
                
            
        