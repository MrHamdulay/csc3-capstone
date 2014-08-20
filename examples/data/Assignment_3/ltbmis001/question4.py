import math
x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for num in range(x+1,y):
    isPrime=True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            isPrime=False     
    if isPrime==True and str(num)==str(num)[::-1]:
        print(num)
          



    
        
        


