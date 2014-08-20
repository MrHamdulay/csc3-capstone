#Program To Find Palendromic Primes
#BNCDEA001

def main():
    n=eval(input("Enter the starting point N: \n"))
    m=eval(input("Enter the ending point M: \n"))
    print("The palindromic primes are:")
    if n==1:
        print("2")
    
    for i in range(n+1,m):
        if str(i)==str(i)[::-1]:
            p=2
            p=p+1
            for p in range(2,i):
                if p==i:
                    continue
                if i%p==0:
                    break
            if i%p==True:
                print(i)
                
                    
                
                    
                    
                
                
                    
                    
            
            
            
            
            
            #r=2
            #if r!=i and r!=1 and r<m:
             #   for r in range(1,m):
              #     elif i%r==True:
                #        print(i)
    
                
                
                #for r in range(2,m+1):
                 #   if i%r>=0:
                  #      print(i)
                        
                
                    
                
                
            
            
            
            
            #for p in range(2,m):
             #   if i%p==True:
              #      print(i)
        
main()

