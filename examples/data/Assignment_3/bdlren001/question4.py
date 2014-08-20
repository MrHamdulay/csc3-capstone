# a program to find the palidromic numbers
# Budeli Rendani
# BDLREN001
# 26 March 2014

def palidromics():
    
    start_N=eval(input("Enter the starting point N:\n"))
    end_M=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    
    for e in range(start_N+1,end_M):
        b = str(e)
        c = b[::-1]
        
        if b == c:
            
            for d in range(2,end_M):
                if e==d:
                    print(e)
                else:
                    if e%d == 0:
                        break
                
palidromics()