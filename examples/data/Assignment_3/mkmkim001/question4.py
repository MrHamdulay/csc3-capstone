low=eval(input("Enter the starting point N:\n"))
high=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range (low+1,high):
    if (-1<=i<=1): continue
    x=i
    for j in range(2,i):
        if i%j==0: break
    else:
        st=str(i)
        rev=st[::-1]
        if st==rev:
            print(i)