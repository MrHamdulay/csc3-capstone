N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
if N<=2 and M>=3:
    print(2)
count = 0
for i in range(N+1,M):
    i = str(i)
    if i==i[::-1]:
        i = int(i)
        for x in range(2,i):
            if i%x!=0:
                count+=1
            if i%x==0:
                count=0
                break
            if count==i-2:
                print(i)
                count=0