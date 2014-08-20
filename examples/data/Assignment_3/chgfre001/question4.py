def palindrome():
    
    n=eval(input('Enter the starting point N:\n'))
    m=eval(input('Enter the ending point M:\n'))
    print('The palindromic primes are:')
    n=n+1

    for i in range(n,m):
        x=True
        for k in range(2,(i)):
            if int(i)%k==0:
                x=False
            
        if x==True:
            if str(i)[::-1]==str(i):
                print(i)
               
palindrome()               
        