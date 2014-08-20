
import math

def palindrome(start,stop):
    
    print("The palindromic primes are:")
    
    conv = ""
    
    if start < 2:
        
        print("1 is not considered as a prime number")
        
    if start % 2 == 0:
        
        for i in range(start+1,stop,2):
            
            change = ""+str(i)
            
            # print(change)
            
            for j in range(len(change)-1,-1,-1):
                
                conv += str(change[j])
                
            
                
            if str(change) == str(conv):
                
                change = int(change)
                
                sqrt_change = (int(math.sqrt(change)))+1
                
                for k in range(3,sqrt_change,2):
                    
                    cond = False
                    
                    if change % k == 0:
                        
                        continue
                    
                    else:
                        
                        cond = True
                        
                if cond == True:
                    
                    print(change)
                  
            conv = ""
                
st = eval(input("Enter the starting point N:\n"))
sp = eval(input("Enter the ending point M:n"))
palindrome(st,sp)