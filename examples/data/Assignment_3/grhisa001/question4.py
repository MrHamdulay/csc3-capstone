def main():
    x = eval(input("Enter the starting point N: \n"))
    y = eval(input("Enter the ending point M: \n"))
    print("The palindromic primes are:")
    k=1
    
    
    for i in range(x+1,y):
        
        if str(i)==str(i)[::-1]:
            
            for k in range(2,i):
                if k == i:
                    continue
                
                if i%k == False:
                    break
                
            if i%k == True:
                    print(i)
    
               
            
            
    
main()