M=eval(input("Enter the starting point N:\n"))
N=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for num in range(M+1,N):
    prime = True
    for i in range(2,int((num)**0.5+1)):
        if (num%i==0):
            prime = False
        if num == M:
            prime= False  
    if prime :
        if num>1:
    
            if str(num) == str(num)[::-1]:
             print(num)