#program to find all palindramic primes between two integers
#vuyolwethu nkosi
#26 march 2014

def palindromic_prime():
    starting=eval(input("Enter the starting point N:\n"))
    ending=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(starting+1,ending):
        if (i==2):
            print(i)
        if(i%2!=0):
            a=str(i)
            if(a==a[::-1]):
                k=2
                while (k<i-1):
                    k+=1
                    if i%k==0:
                        break
                else:
                    print(i)

palindromic_prime()
    
        