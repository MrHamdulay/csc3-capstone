def ndom_to_decimal (num):
   temp= num//1000
   temp2=num//100 - temp
   temp3=num//10 - temp2*10
   temp4=num - temp2*100 - temp3*10  
   
   return  (temp2*6 + temp3) *6 +temp4
   
def decimal_to_ndom (num):
   temp = num//6
   c = num - temp*6
   temp2 = temp//6
   c2 = temp - temp2*6  
   temp3 = temp2//6
   c3 = temp2 - temp3*6
   temp4 = temp3//6
   c4 = temp3 - temp4*6
   return  c4*1000+ c3*100 + c2*10 +c

def ndom_add (a, b):
   return decimal_to_ndom (ndom_to_decimal (a)+ndom_to_decimal(b))

def ndom_multiply (a, b):
   return decimal_to_ndom (ndom_to_decimal (a)*ndom_to_decimal(b))