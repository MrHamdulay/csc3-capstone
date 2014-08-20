# 24 March 2014
# Jaren Hendricks
# Program to find all palindromic primes

Start = eval (input("Enter the starting point N:\n"))
End = eval (input("Enter the ending point M:\n"))
print ("The palindromic primes are:")

for k in range(Start+1, End):
    Sum = 0
    prime = True
    j = k
    while k!= 0:
        mod = k%10
        k = k//10
        Sum = (Sum * 10) + mod
    if j == Sum:
        for i in range(2,j-1):
            if j%i == 0:
                prime = False
        if prime == True: 
            print(j)
