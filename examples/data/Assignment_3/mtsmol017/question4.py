b=eval(input("Enter the starting point N:\n"))
c=eval(input("Enter the ending point M:\n"))
result=[]
for i in range(b,c):
    if str(i)==(str(i))[-1::-1]:
        factors=0
        for m in range(2,10):
            if i%m==0:
                factors+=1
        if factors<1:
            result.append(i)
print("The palindromic primes are:")
for p in result:
    print(p)