x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(x+1,y):
    z=True
    for j in range (2, i//2+1):
        if (i%j == 0):
            z = False
            break
    if z:
        i=str(i)
        if i!=i[::-1]:
            z=False
    if z:
        print(i)
        
            
            
            
        
    
