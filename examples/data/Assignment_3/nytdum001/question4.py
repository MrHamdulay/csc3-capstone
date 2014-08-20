def pal():
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(n+1,m):
        prime=1
        for j in range(2,i-1):
            if (i%j==0):
                prime=0
                break
        r=str(i)
        s=r[::-1]
        if s==r and prime==1:
            print(s)
pal()