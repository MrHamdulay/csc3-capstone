def palin():
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(N+1,M):
            prime = True
            for j in range(2,i-1):
                if (i%j==0):
                    prime = False
                    break
            if prime:
                r=str(i)
                s=r[::-1]
                if s==r:
                    print(s)
palin()
            