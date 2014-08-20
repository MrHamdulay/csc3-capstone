def ndom_to_decimal (a):
    
    
   a = str(a)
   sum = 0
   for i in range (len(a)):
      sum += int(a[i])*6**(len(a)-1-i)
   return sum
   

def decimal_to_ndom (a):
   
   rem = ""

   while a!=0:
      rem += str(a%6)
      a = (a//6)
      
   return (rem[::-1])
   
   

def ndom_add (a, b):
   t = ndom_to_decimal (a)
   y = ndom_to_decimal (b)
   return(decimal_to_ndom (t+y))
   
   
   
def ndom_multiply (a, b):
   t = ndom_to_decimal (a)
   y = ndom_to_decimal (b)
   return(decimal_to_ndom (t*y))
        
    