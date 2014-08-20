from math import floor,log10



def decimal_to_ndom (a):
    
   total = 0
   base = 1
   
   for i in range(0,4):
      rem = floor((a%6)) * base 
      a = a/6      
      base = base * 10
      total = total + rem
      
   return total



def ndom_to_decimal(a):
   
   total = 0   
   increment = 0
   
   for i in str(a):
      total = increment * 6
      increment = total+eval(i)
         
   return increment
           

def ndom_add(a,b):
   
   one = ndom_to_decimal(a)
   two = ndom_to_decimal(b)
   answer = one + two
   
   final = decimal_to_ndom(answer)
   return final

def ndom_multiply(a,b):
   
   one = ndom_to_decimal(a)
   two = ndom_to_decimal(b)
   answer = one * two
   
   final = decimal_to_ndom(answer)
   return final
   


      

      
   
      
      