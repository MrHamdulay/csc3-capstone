N=eval(input("Enter the starting point N:"'\n'))
M=eval(input("Enter the ending point M:"'\n'))

def p_primes():
    for i in range((N+1),M):
        i=str(i)
        r=i[::-1]
        if i==r:
            for x in range(2,M):
                if int(i)!=x:
                    if int(i)%x==0:
                        break
                else:
                    print(i)
                    
print("The palindromic primes are:")
p_primes()
                        
    
