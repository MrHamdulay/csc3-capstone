N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(N+1,M):
    ii=str(i)
    keep=0
    for j in range((len(ii)//2)+1):
        if ii[j]==ii[len(ii)-j-1]:
            keep=1
        else:
            keep=0
        if keep==0: break
    if keep==1:
        a=2
        notprime=0
        while i > a :
            if i%a==0 & a!=i:
                notprime=1
                break
            a=a+1
        if notprime!=1 and i!=1:
            print(i)
                 
