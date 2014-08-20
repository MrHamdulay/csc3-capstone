n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(n+1,m):#loop through the range given
    q=i
    p=0
    while(q!=0):#check palindrome
        p=q%10+p*10
        q=q//10
    if(i==p):
        for x in range(2, p): #check prime
                if p % x == 0:
                    break
        else:
            print(p)