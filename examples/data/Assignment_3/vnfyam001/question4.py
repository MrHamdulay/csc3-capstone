import math
x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(x+1,y):
  #print(i)
  t=str(i)
  y=t[::-1]
  
  if(y==t and i!=1):
    count=0
    r=eval(t)
    y=math.sqrt(r)
    re=round(y)
    
    v=1
    while re>=v:
      if(r%v==0):
        count=count+1 
      v=v+1
      
      
    if(count==1):
      print(r)
   


  