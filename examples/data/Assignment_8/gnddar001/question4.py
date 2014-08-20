import math
import sys
sys.setrecursionlimit (30000)           
    
def my_way(k,m): 
    if k<=m:
        
        testing_drome=int(drome(k,"")) 
        
        if testing_drome==k:  
            testing=find_prime(k,2,"") 
            
            if testing!="Not":
                print(k) 
        
        my_way(k+1,m) 
        
def find_prime(k,w,v):
    
    if(k==1):
        return (v+"Not")
    
    sqroot=int(math.sqrt(k)) 
    
    if(w!=(sqroot+1)): 
        
        if(k%w!=0): 
            return find_prime(k,w+1,v) 
        
        else:
            return (v+"Not")         
        
def drome(a,trial): 
    
    if(len(str(a))!=1): 
        d=a%10  
        trial+=str(d) 
        return drome((a-(a%10))//10,trial)
    
    else:
        return(trial+str(a))        
        
if __name__== "__main__":
    
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    
    print("The palindromic primes are:")
    
    my_way(n,m)
    
    
    