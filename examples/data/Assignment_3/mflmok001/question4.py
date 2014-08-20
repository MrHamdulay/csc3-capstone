def palin_primes():
    start=eval(input("Enter the starting point N:\n"))
    end=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(start+1,end):
        for j in range(2,i):
            if (i%j==0):
                break  
        else:    
            if str(i)[::1]==str(i)[::-1]:
                print(i)
                
palin_primes()
