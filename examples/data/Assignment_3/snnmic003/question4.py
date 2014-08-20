#Question 4

N = eval (input ("Enter the starting point N:\n"))
M = eval (input ("Enter the ending point M:\n"))

print ("The palindromic primes are:")

for i in range (N+1, M):
    j = i
    holder = ""
    while j:
        holder += str (j%10)
        j = int (j/10)
        
    if (holder == str (i)):
        factor = 0
        for k in range (1, i):
            if (i % k == 0):
                factor += 1
        if (factor == 1):
            print (i)