n = eval(input("Enter the starting point N:\n"))
m= eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")


for num in range (n+1,m):
    num1= str(num)
    prime = True
    rev = ""
    
    for i in range(len(num1),0,-1):
        rev = rev + (num1[i-1])
        
    if rev == num1:
        for k in range(2,num):
            if num%k == 0:
                prime = False
                
        if prime == True:
            print(num)