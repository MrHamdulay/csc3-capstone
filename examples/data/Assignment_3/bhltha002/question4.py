x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
n=(x,y)
print("The palindromic primes are:")

for i in range(x+1,y):
    n=str(i)
    reverse=n[::-1]
    if n==reverse:
        palindrome=True
    else: palindrome=False
    #if str(n)==str(n)[::-1]:
        
    n=True
    for j in range (2,i):
        if i%j==0:
            prime=False
            break
        else:
            prime=True
    if prime and palindrome:
        print(i)
        
    
    
    