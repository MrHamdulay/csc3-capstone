x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
c=0
r=x
print("The palindromic primes are:")
for i in range(x+1,y):
    c=0
    for j in range(2,y):
        if i%j==0: 
            c=c+1
    if c==1:
        r=str(i)
        if r==r[::-1]:
            print(i)