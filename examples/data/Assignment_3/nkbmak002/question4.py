def cake(a,b):
    
    for a in range(a+1,b):
        for j in range(2,a):
            if a%j == 0:
                break
        else:
            p = str(a)
            if p == p[::-1]:
                q = int(p)    
                if q<2: continue
                else:
                    print(q)
            
if __name__== '__main__':
    a= eval(input("Enter the starting point N:\n"))
    b = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    
    
    cake(a,b)