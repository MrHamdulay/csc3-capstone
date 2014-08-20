n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for nmbr in range(n+1,m):
    if nmbr>1:
        for i in range(2,nmbr):
            if (nmbr%i)==0:
                break
        else:
            x=str(nmbr)
            if nmbr==eval(x[::-1]):
                print(nmbr)
            else:
                continue
    else:
        continue