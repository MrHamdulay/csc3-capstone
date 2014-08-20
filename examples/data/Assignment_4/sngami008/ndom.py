def ndom_to_decimal(ndom):
   
   x = ndom%100
   q = x%10
   decimal = ( (ndom//100)*36 ) + ( (x//10)*6 ) + q
   
   return decimal

def decimal_to_ndom(dec):
   
   x = dec%36
   q = x%6
   ndom = ( (dec//36)*100 ) + ( (x//6)*10 ) + q
   
   return ndom

def ndom_add(a, b):
   
   x = ndom_to_decimal(a)
   q = ndom_to_decimal(b)
   ndomsum = x + q
   
   return decimal_to_ndom(ndomsum)

def ndom_multiply(a, b):
   
   x = ndom_to_decimal(a)
   q = ndom_to_decimal(b)
   ndomproduct = x * q 
   
   return decimal_to_ndom(ndomproduct)
   