#question4
n = eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(n+1,m,1):
    check=0
    for j in range (i):
        if j!=0:
            if (i%j==0):
                check+=1
    if check<2:

            we=str(i)#we is a string now
            l=len(we)
            rev=we[-1:0:-1]+we[0]
            rev=int(rev)
            if rev==i:
                print(i)