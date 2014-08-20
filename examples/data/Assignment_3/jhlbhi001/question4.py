x=eval(input("Enter the starting point N: \n"))
y=eval(input("Enter the ending point M: \n"))
print("The palindromic primes are: ")

if x<2:
    print(2)
for i in range (x+1,y,1):
    n=str(i)
    if n==n[::-1]:
        n=int(n)
        for m in range (2,n):
            if n%m==0:
                break
            elif m==(n-1):
                print(n-1)
                print(n)
                
                
