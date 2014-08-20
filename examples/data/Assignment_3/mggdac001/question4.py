import math
x=eval(input('Enter the starting point N:\n'))
y=eval(input('Enter the ending point M:\n'))
print("The palindromic primes are:")
for num in range(x,y):
    prime = True

   
    for i in range(2,num//4):
        if (num%i==0):
            prime = False
    if prime:
        final=str(num)
        reverse=final[::-1]
        if final==reverse:
            print(final)
            
                


            
                