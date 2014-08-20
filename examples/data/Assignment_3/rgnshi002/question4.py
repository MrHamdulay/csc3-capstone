x = eval(input("Enter the starting point N:\n"))
y = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(x+1,y):
    j = str(i)
    z = j[::-1]
        
    if j == z:    
        
        for r in range(2,y):
            if i==r:
                print(i)
            else:
                if i%r == 0:
                    break
    

