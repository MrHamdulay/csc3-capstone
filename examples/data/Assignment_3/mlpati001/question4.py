#ATISANG MOLAPO
#STUDENT NUMBER:MLPATI001
#A program to find all palindromic primes between two integers supplied as input (start and end points are excluded).
def palindromic():
    a=eval(input("Enter the starting point N:\n"))
    b=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    
    for i in range(a+1,b):
        k = str(i)
        l = k[::-1]
        
        if k == l:
            
            for j in range(2,b):
                if i==j:
                    print(i)
                else:
                    if i%j == 0:
                        break
                


palindromic()