# Find palindromic primes within an interval
# Danielle Sher

import sys
sys.setrecursionlimit(30000)

a = input("Enter the starting point N:\n")
b = input("Enter the ending point M:\n") 
if a == '' and b == '':
    print()

else:
    z = int(a)    
    y = int(b)
    print("The palindromic primes are:")
    i = 2
    def primechecker(z):
        global i
    
        if z == y+1:
            return "" 
        if z == 2:
            print (z)
            i = 2
            return primechecker(z + 1)   
    
        if z % i == 0 and z > i or z%2 == 0 or z<2:
            i = 2
            return primechecker(z + 1)
    
   
        elif z > i and z%i != 0:
            i = i + 1
            return primechecker(z)
        
        elif len(str(z)) == 1:
            print (z)
            return primechecker(z + 1) 
    
        elif z == i:
            d = str(z)
            e = list(d)
            e.reverse()
            f = "".join(e)
            if d == f:
                print (z)
            i = 2
            return primechecker(z + 1)          
        
        else:
            d = str(z)
            e = list(d)
            e.reverse()
            f = "".join(e)
            if d == f:            
                print (z)
            i = 2
            return primechecker(z + 1)         
        
         
        
    
          
        

    print(primechecker(z))  
    
        