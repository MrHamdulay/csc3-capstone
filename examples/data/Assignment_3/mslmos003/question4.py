def pal():
    start = eval(input("Enter the starting point N: \n"))
    end = eval(input("Enter the ending point M: \n"))
    print("The palindromic primes are:") 
    
    start += 1 
    backwards = str(start)[::-1]
    while start < end:
        if str(start) == backwards:
            for i in range(2, start):
                if start % i == 0:
                    break
            else:
                print(start)
                
        start += 1
        backwards = str(start)[::-1]
        
pal()

        