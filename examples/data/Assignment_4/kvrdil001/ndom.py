def ndom_to_decimal(ndom):
   
   x = ndom%100
   y = x%10
   decimal = ( (ndom//100)*36 ) + ( (x//10)*6 ) + y
   
   return decimal

def decimal_to_ndom(dec):
   
   x = dec%36
   y = x%6
   ndom = ( (dec//36)*100 ) + ( (x//6)*10 ) + y
   
   return ndom

def ndom_add(a, b):
   
   x = ndom_to_decimal(a)
   y = ndom_to_decimal(b)
   ndomsum = x + y
   
   return decimal_to_ndom(ndomsum)

def ndom_multiply(a, b):
   
   x = ndom_to_decimal(a)
   y = ndom_to_decimal(b)
   ndomproduct = x * y 
   
   return decimal_to_ndom(ndomproduct)
   