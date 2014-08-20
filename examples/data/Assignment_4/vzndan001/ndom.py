#This converts a base 6 ndom number to our normal numbers
def ndom_to_decimal(a):
     a=str(a)
     lendom=len(a)
     n=2
     c=0
     e=0
     
     if lendom==3:
          for i in a:
               newi=int(i)
               b=newi*(6**n)
               c+=b
               n=n-1
          return c
     
     elif lendom==2:
          for i in a:
               newi=int(i)
               d=newi*(6**(n-1))
               e+=d
               n=n-1
          return e
     
     elif lendom==1:
          if a==1:
               return(1)
          if a==2:
               return(2)
          if a==3:
               return(3)
          if a==4:
               return(4)
          if a==5:
               return(5)     

                    
               
        

#this converts our normal numbers to base 6 ndom numbers        
def decimal_to_ndom(a):
     
     

     if a==1:
          return(1)
     if a==2:
          return(2)
     if a==3:
          return(3)
     if a==4:
          return(4)
     if a==5:
          return(5)

     elif a>=90:
          a=int(a)
          b=(a//36)
          c=b*36
          d=a-c
          e=d//6
          f=e*6
          g=d-f
          h=g//1
                  
          nn=str(b)+str(e)+str(h)
          nn=int(nn)
          return(nn)            
    
     elif a<90:
          a=int(a)
          j=a//6
          k=j*6
          l=a-k
          m=l//1
          nn=str(j)+str(m)
          nn=int(nn)
          return(nn)
     
     
def ndom_add(a,b):   
     a=ndom_to_decimal(a)
     b=ndom_to_decimal(b)
     add=a+b
     return decimal_to_ndom(add)  
    
def ndom_multiply(a,b):
     a=ndom_to_decimal(a)
     b=ndom_to_decimal(b)
     times=int(a)*int(b)
     return decimal_to_ndom(times) 
    

    

    
