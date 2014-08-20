# Assignment 3, question 4
# Danielle Sher
# 19 March 2014

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

if m > n >= 1:
    for i in range(n+1, m):
        prime = True 
        for j in range (2, i):
            if i % j == 0:
                prime = False
        if prime:
            if str(i) == str(i)[::-1] and str(1) !=1:
                print(int(i))


                
        
    
    
        
    


     
           