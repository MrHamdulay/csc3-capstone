def mrPrime():
    start=eval(input("Enter the starting point N:\n"))
    end=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(start+1,end):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                k=str(i)
                if k==k[::-1]:
                    print(i)
mrPrime()