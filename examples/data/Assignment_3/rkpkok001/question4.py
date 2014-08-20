x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
def palindrome(x,y):
    print("The palindromic primes are:")
    for i in range(x+1,y):
        k=str(i)
        if k==k[::-1]:
            for j in range(2,i):
                if (i%j==0):
                    break
            else:
                print(i)
palindrome(x,y)