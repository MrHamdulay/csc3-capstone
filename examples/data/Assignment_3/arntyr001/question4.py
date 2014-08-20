def Prime(n):
    if n==2:
        return True
    elif n%2==0:
        return False
    for j in range(3,n//2+2):
        if n%j==0:
            return False
        
    return True



N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N+1,M):
    if Prime(i)==True and str(i)==str(i)[::-1]:
        print(i)

#    for j in range(2,M):
#        if i%j==0 and j!=i:
#            break
#        else:
#            while j>=i:
#                if str(i)==str(i)[::-1]:
#                    print(i)
#                    break
                