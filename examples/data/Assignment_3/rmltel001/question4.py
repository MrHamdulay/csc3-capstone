#Palindromic prime numbers

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for i in range(n+1, m):
    num = str(i)
    prime = 1
    revNum = ""
    for j in range(len(num), 0, -1):
        revNum += num[j-1]
   
    if revNum == num:
        for k in range(2, i):
            if i%k == 0:
                prime = 0
                break
               
        if prime == 1:
            print(i)
         
            
    
                
            
    