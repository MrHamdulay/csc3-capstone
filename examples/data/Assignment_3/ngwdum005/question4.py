#Dumisani Ngwenza
#NGWDUM005
#23/03/14
# A program that finds all the palindrome primes between 2 integers supplied as input

N = eval(input("Enter the starting point N:\n"))
M = eval (input("Enter the ending point M:\n"))
print ("The palindromic primes are:")
for i in range(N+1, M):
    point = str(i)
    reverse = point[::-1]
    if point == reverse:
        for k in range (2, i):
            remainder = i%k
            if remainder == 0:
                break
        else: print (i)