#Keegan Naidoo
#NDXKEE009
import math

    
s=eval(input("Enter the starting point N: \n"))

e=eval(input("Enter the ending point M: \n"))

s1=str(s)
e1=str(e)

c=1
     
print("The palindromic primes are:") 

for i in range(s+1,e):
    
      a=s+c
    
      #print(a)
    
      a1=str(a)
    
      #print(a1)
    
      #print(a1[::-1])
  
   
        
      if all(i%x!=0 for x in range(2,int(math.sqrt(i))+1)):
            
            if(a1==a1[::-1]):
            
                  print(a1)
                
      c=c+1

 


    
    
    
    
    