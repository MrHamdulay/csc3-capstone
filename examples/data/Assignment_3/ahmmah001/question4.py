#Mahnoor Ahmed
#AHMMAH001
#Palindromic primes

a=eval(input("Enter the starting point N:\n"))
b=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(a+1,b):
    u=str(i)
    opp=u[::-1]
    if u==opp: 
        diff=i-2
        q=0
        for j in range(2,i):
            rem=i%j
            if rem==0: break
            q=q+1
        if q==diff:
            print(i)
            
                
    


    