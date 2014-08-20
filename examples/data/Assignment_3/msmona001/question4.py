N = eval(input("Enter the starting point N: \n"))
M = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are: ")
for i in range((N+1),M):
    Prime = False
    counter = 0
    if (str(i) == str(i)[::-1]) :
        if i == 2:
            print(i)
        if i % 2 == 0:
            counter +=1
        for j in range(3, i):
            if (i%j) == 0:
                counter +=1
    if counter == 0:
        Prime = True
    
    if (str(i) != str(i)[::-1]) or (Prime == False):
        continue
    print(i)
    
    