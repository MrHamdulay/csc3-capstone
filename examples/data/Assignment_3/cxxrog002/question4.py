import math

a=eval(input("Enter the starting point N:\n"))
b=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range((a+1),b):
    word =str(i)
    rev=word[::-1]
    if(word==rev):
        isPrime=True
        for x in range(2,int(math.sqrt(i))+1):            
            if (i%x==0):
                isPrime=False
                break
        if  isPrime:
            print(i)
         
        
