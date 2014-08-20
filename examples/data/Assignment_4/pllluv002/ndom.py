def ndom_to_decimal(x):
   
      a=(x//100)
      b=a*36
      c=(((x-(a*100))//10))
      d=c*6
      e=x-(a*100+c*10)
      q=b+d+e
      return(q)
      
   
   
   
def decimal_to_ndom(x):
      a=(x//36)
      b=a*100
      c=(((x-(a*36))//6))
      d=c*10
      e=x-(a*36+c*6)
      q=b+d+e
      return(q)
      
   
   
def ndom_add(x,y):
   
      a=(x//100)
      b=a*36
      c=(((x-(a*100))//10))
      d=c*6
      e=x-(a*100+c*10)
      p=b+d+e   
      
      a=(y//100)
      b=a*36
      c=(((y-(a*100))//10))
      d=c*6
      e=y-(a*100+c*10)
      q=b+d+e  
      
      u=q+p
      
      a=(u//36)
      b=a*100
      c=(((u-(a*36))//6))
      d=c*10
      e=u-(a*36+c*6)
      return(b+d+e)   
      
   
def ndom_multiply(x,y):
   
      a=(x//100)
      b=a*36
      c=(((x-(a*100))//10))
      d=c*6
      e=x-(a*100+c*10)
      p=b+d+e   
      
      a=(y//100)
      b=a*36
      c=(((y-(a*100))//10))
      d=c*6
      e=y-(a*100+c*10)
      q=b+d+e  
      
      u=q*p   
      
      a=(u//36)
      b=a*100
      c=(((u-(a*36))//6))
      d=c*10
      e=u-(a*36+c*6)
      return(b+d+e)     