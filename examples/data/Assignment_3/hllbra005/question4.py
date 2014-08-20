start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range (start+1, end):
    isPalidrome = False
    canPrint = True
    if str(i)[::-1] == str(i):
        isPalidrome = True
    
    for j in range (2,9999):
        if i%j == 0:
            if j !=i:
                canPrint = False
                
            
    if isPalidrome is True and canPrint is True:
        print(i)
        
        
        