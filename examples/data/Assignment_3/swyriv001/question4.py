N=eval(input("Enter the starting point N:""\n"))
M=eval(input("Enter the ending point M:""\n"))
print("The palindromic primes are:")


for n in range(N+1,M):
  if n>1:
    for x in range(2,n):
      if n%x == 0:
        break
    else:
        c=str(n)
        if c==c[::-1]:
            print(n)
        
                