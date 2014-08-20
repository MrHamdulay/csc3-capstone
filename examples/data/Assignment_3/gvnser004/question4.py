s=eval(input("Enter the starting point N:\n"))
e=eval(input("Enter the ending point M:\n"))
p=""
t=""

print("The palindromic primes are:")

for i in range(s+1,e):
    
    t=0
    if(str(i)==str(i)[::-1]):
        for j in range(2,i):
            if (i%j==0):
                t+=1
        if(t==0):
            print(i)

        
    
    
        