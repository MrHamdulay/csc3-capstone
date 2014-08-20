x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are: ")

if x<2:
    print (2)
for i in range (x+1,y,1):
    a=str(i)
    if a==a[::-1]:
        a=int(a)
        for j in range (2,a):
            if a%j==0:
                break
            
            elif j==(a-1):
                print(a)
                 

    
        
    