sp=eval(input("Enter the starting point N:\n"))
ep=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for num in range(sp+1,ep):
    
    isprime=True
    if num == 1:
        continue
        
    
    else : 
        for i in range (2, num):
            if num%i == 0:
                isprime = False
                break
    
        if isprime==True and str(num)[::-1]==str(num):
            print(num)    
    

    