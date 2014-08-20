def palprimes():
    
    first = eval(input("Enter the starting point N: \n"))
    last = eval(input("Enter the ending point M: \n")) 
    print("The palindromic primes are:")
       
    first += 1    
    reverse = str(first)[::-1]     
   
    while first < last: 
        if str(first)==reverse:  
            for i in range(2, first):
                if first % i==0: 
                    break  
            else:        
                print(first)            
        first += 1 
        reverse = str(first)[::-1] 
palprimes()