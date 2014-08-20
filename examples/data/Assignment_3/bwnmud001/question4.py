x=eval(input("Enter the starting point N: \n"))
y=eval(input("Enter the ending point M: \n"))
count=0
print("The palindromic primes are:")
for i in range (x,y+1):
    a=str(i)
    b=a[: :-1]
    if a==b:
        for j in range(2,int(i)):
            if int(i)%j==0: break
        print(i)
    
    