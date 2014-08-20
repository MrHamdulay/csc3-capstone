start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range (start+1,end):
    S=str(i)
    s_rev=S[::-1]
    if s_rev==S:
        
    #print(i)
        for j in range(2,end):
            if i==j:
                print(i)
                break
            if i%j == 0:
                break
            
    

    
            
     