import math
N = eval(input("Enter the starting point N: \n"))
M = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
for i in range(N+1, M):
    number = str(i)
    reverse = number[::-1]   
    prime = True
    if number == reverse:  
        for k in range(2,int(math.sqrt(i))+1):
            if i%k == 0:
                prime = False
                break
        if prime ==True:
            print(i)
         
              