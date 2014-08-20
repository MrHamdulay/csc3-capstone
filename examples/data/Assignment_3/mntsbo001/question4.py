def main():
    start=eval(input("Enter the starting point N:\n"))
    end=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    a=0
    for i in range(start,end):
        rev=str(i)[len(str(i))::-1]
        if i==rev:
            for j in range(1,j):
                a=i%j
                if a==0:
                    a+=1
            if a==2:
                print(i)
            a=0
            
                    

        
        
        
main()        