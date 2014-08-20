def palindromic_prime():
    start=eval(input("Enter the starting point N:\n"))
    end=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range (start+1,end):
        if i==2:
            print(i)
        if (i%2!=0):
            a=str(i)
            if(a==a[ : :-1]):
                l=2
                while l<i-1:
                    l+=1
                    if i%l==0:
                        break
                else:
                    print(i)
palindromic_prime()
    
                