# Palindromic primes between 2 integers
# Kristin Kinmont
# 21 March 2014

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N+1,M):
    p = str(i)
    rev = p[-1::-1] 
    if p==rev:
        count = 0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0:
            print(i)
            