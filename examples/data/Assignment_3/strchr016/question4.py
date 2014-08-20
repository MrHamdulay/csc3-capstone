N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N+1,M):
    factor=0
    for j in range(1,i):
        if i%j==0:
            factor+=1
            if factor>1:
                break
    if factor==1:
        if str(i)[::-1]==str(i):
            print(i)
        else:
            continue
