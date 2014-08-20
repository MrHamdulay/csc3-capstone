def main():
    
    n= eval(input("Enter the starting point N:\n"))
    m= eval(input("Enter the ending point M:\n")) 
    print("The palindromic primes are:")        
        
    for i in range(n+1,m):
        for s in range(2,i):
            if i%s==0: break
          
          
        else:
            i=str(i)
            rev=i[::-1]
            if i==rev:
                print(i)              
                   
main()