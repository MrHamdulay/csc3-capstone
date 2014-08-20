n = eval(input("Enter the starting point N: \n"))
m = eval(input("Enter the ending point M: \n"))
start = n
end =m
print("The palindromic primes are:")
r=0
lo = m-n
for i in range(lo):
    s=str(n)
    s = s[::-1]
    r=0
    g=2
    if str(s)==str(n):
        for d in range(n):
            v=n/(g)
            roun = int(v)
            roun2= roun*(g)
            if g == n:
                break  
            if roun2==n:
                r=1  
            g=g+1
        if r==0:
            if n!=start and n!=end:
                print(str(n))
    n = n+1