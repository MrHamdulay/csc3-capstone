s= eval(input('Enter the starting point N:\n'))
e= eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:\n',end='')
for d in range(s,e):
    i = str(d)
    i_rev = i[::-1]
    if i_rev==i:
        for m in range(2,e):
            if d == m:
                print(d)
               
                
            elif d%m==0:
                break 
            
          
            
             
        
    
 
    
    
   
    
    
     