n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
def drome():
    for i in range(n+1, m):
        i=str(i)
        b=i[::-1]
        if i==b:
            for y in range(2, m):
                if int(i)!=y:
                    if int(i)%y==0:
                        break
                else:
                    print(i)
print("The palindromic primes are:")
drome() 
