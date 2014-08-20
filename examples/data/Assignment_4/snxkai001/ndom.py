#ndom to decimal
def ndom_to_decimal(a):
   bat= len(str(a))
   a= str(a)
   if (1 <=bat< 2):
      ceed=eval(a)
      d=(ceed*6)+0
      return d
     
   if (2 <=bat< 3):
      edd=eval(a[0:1])
      fol=(edd*6)
      got=eval(a[1:2])
      h=fol+got
      return h
     
   if (3 <=bat< 4):
      imp=eval(a[0:1])
      j=(imp*6)
      kn=eval(a[1:2])
      l=j+kn
      m=(l*6)
      n=eval(a[2:3])
      o=m+n
      return o
      
      

def decimal_to_ndom(a):
   bat=len(str(a))
   
   if (1 <=bat< 2):
      c=a//6
      d=a%6
      return d
    
   if (2 <=bat< 3):
      if a<35:
         e=a//6
         f=a%6
         g=e//6
         h=e%6
         p=str(h)+str(f)
         return p
      if a>35:
         e=a//6
         f=a%6
         g=e//6
         h=e%6
         i=g%6
         p=str(i)+str(h)+str(f)
         return p
         
      
    
   if (3 <=bat< 4):
      i=a//6
      j=a%6
      k=i//6
      l=i%6    
      m=k//6
      n=k%6
      o=m//6
      p=m%6
      if p==0:
         z=str(n)+str(l)+str(j)
         return z
         
      else:
         z=str(p)+str(n)+str(l)+str(j)
         return z
         


     
def ndom_add(num1, num2):
   x=ndom_to_decimal(num1)
   y=ndom_to_decimal(num2)
   p=int(x)+int(y)
   printing=decimal_to_ndom(p)
   return printing

def ndom_multiply(num1, num2):
   ndomd=ndom_to_decimal(num1)
   ndomd2=ndom_to_decimal(num2)
   p=int(ndomd)*int(ndomd2)
   answer=decimal_to_ndom(p)
   return answer
   