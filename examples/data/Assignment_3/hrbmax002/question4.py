n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")



for i in range (n+1,m):
    x = True
    if str(i)!=str(i)[::-1]:
        x= False
    else:    
     for j in range (2,i):
       if i%j == 0:
            x = False
    if x:
        print (i)
    
    
             
