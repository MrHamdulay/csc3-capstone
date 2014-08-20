def decimal_to_ndom(a):
   c=a//6
   d=a%6
   s=c//6
   e=c%6
   f=s%6
   foxes=""
   if f==0:
      pinkjam=str(e)
      queen=str(d)
      foxes+=pinkjam+queen
   else:
      pinkjam=str(e)
      queen=str(d)
      beat=str(f)
      foxes+=beat+pinkjam+queen
   return (int(foxes))
      
def ndom_to_decimal(a):
   b=str(a)
   b=str(a)
   c=0
   t=0
   x=0
   f=len(b)
   k=2
   if f==3:
      for i in range(f):
         j=b[c]
         #c+=1
         d=int(j)*6**k
         x+=d
         c+=1
         k-=1
         #print(x)
      #return(x)
   elif f==2:
      for i in range(1,-1,-1):
         j=b[c]
         d=int(j)*6**i
         x+=(d)
         c+=1 
   return(x)
      
def ndom_add(a,b):
   
   y=str(a)
   x=str(b)
   e=len(y)
   z=len(x)
   if e==3 and z==3:
      j=y[0]
      s=y[1]
      t=y[2]
      q=x[0]
      w=x[1]
      r=x[2]
      d=(int(j)*36+int(s)*6+int(t)*1)+(int(q)*36+int(w)*6+int(r)*1)
   if e==3 and z==2:
      j=y[0]
      s=y[1]
      t=y[2]
      q=x[0]
      w=x[1]
      d=(int(j)*36+int(s)*6+int(t)*1)+(int(q)*6+int(w)*1)
   if e==2 and z==3:
      j=y[0]
      s=y[1]
      q=x[0]
      w=x[1]
      r=x[2]      
      d=(int(j)*6+int(s)*1)+(int(q)*36+int(w)*6+int(r)*1)
   if e==2 and z==2:
      j=y[0]
      s=y[1]
      q=x[0]
      w=x[1]
      d=(int(j)*6+int(s)*1)+(int(q)*6+int(w)*1)
   
   for i in range(1):
      mim=d  
      c=mim//6
      i=mim%6
      h=c//6
      g=c%6
      l=h%6
      happiness=""
      if l==0:
         t=str(g)
         w=str(i)
         happiness+=t+w
      else:
         t=str(g)
         w=str(i)
         r=str(l)
         happiness+=r+t+w
      return(int(happiness))
         
def ndom_multiply(a,b):
   y=str(a)
   x=str(b)
   e=len(y)
   z=len(x)
   if e==3 and z==3:
      j=y[0]
      s=y[1]
      t=y[2]
      q=x[0]
      w=x[1]
      r=x[2]
      d=(int(j)*36+int(s)*6+int(t)*1)*(int(q)*36+int(w)*6+int(r)*1)
   if e==3 and z==2:
      j=y[0]
      s=y[1]
      t=y[2]
      q=x[0]
      w=x[1]
      d=(int(j)*36+int(s)*6+int(t)*1)*(int(q)*6+int(w)*1)
   if e==2 and z==3:
      j=y[0]
      s=y[1]
      q=x[0]
      w=x[1]
      r=x[2]      
      d=(int(j)*6+int(s)*1)*(int(q)*36+int(w)*6+int(r)*1)
   if e==2 and z==2:
      j=y[0]
      s=y[1]
      q=x[0]
      w=x[1]
      d=(int(j)*6+int(s)*1)*(int(q)*6+int(w)*1)
   #return(d)
    
   for i in range(1):
      mim=d  
      c=mim//6
      i=mim%6
      h=c//6
      g=c%6
      l=h%6
      x=""
      if l==0:
         p=str(g)
         q=str(i)
         x+=p+q
      else:
         p=str(g)
         q=str(i)
         n=str(l)
         x+=n+p+q  
      return (int(x))
   