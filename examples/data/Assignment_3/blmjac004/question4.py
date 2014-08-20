import math
start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start+1, end):
    x=str(i)
    if (x[::-1]==x): #number is a palindrome
        prime=1
        for j in range(2,int(math.sqrt(i)+1),1):  #number is a prime
            if (i%j==0):
                prime=0
        if (prime==1):
            print(i)