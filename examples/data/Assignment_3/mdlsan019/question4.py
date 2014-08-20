#Sanele Mdlalose
#MDLSAN019
#question4

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for j in range(N+1,M):
    for i in range(2,j):
        if (j%i==0):
            break
    else:
        if str(j)==str(j)[::-1]:
            print(j)
    
    