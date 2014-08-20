#import math

start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def prime(i):
      for s in range(2,i):
            if (i%s)==0 or s==1:
                  return False
            #print(s)


for j in range(start+1,end):
      n=0
      v=j
      if j>1:
            while j:
                  n=n*10
                  n=n+(j%10)
                  j=j//10
                  if n==v:
            #print(n)
                        if prime(v)!=False: 
                              print(v)            
                  
                  
#for i in range(start,end):
      #if reverse(i)==True:
      
      
                              
              