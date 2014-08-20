import math
start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(start+1,end):
    n=2
    prime=True
    while n<=math.sqrt(i):
        if i%n==0:
            prime=False
            break
        n+=1
    else:
       i=str(i)
       if i==i[::-1]:
                    print(i)
       i=eval(i)









