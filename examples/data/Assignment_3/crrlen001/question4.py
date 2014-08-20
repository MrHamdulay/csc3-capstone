N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
for num in range(N+1,M):
    if all(num%i!=0 for i in range(2,num)):
        k = str(num)
        if k == k[::-1]:
            print(k)
        
            
#Author: Lenard Carroll
#Student Number: CRRLEN001