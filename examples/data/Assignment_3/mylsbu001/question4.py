import math
lowerNumber = eval(input("Enter the starting point N:\n"))
upperNumber =  eval(input("Enter the ending point M:\n"))
change=""
print("The palindromic primes are:")
for i in range(lowerNumber+1,upperNumber):
      if(i!=1):       
            count=0
            b=2
            sq = math.sqrt(i)
            sq = round(sq)
            while(sq>=b):
                  if(i%b ==0):
                        count=count+1
                  b+=1
            if(count==0 or i==2):
                  change = str(i)
                  change2=change[len(change)::-1]
                  if(change2==change):
                        print(change2) 
            
     