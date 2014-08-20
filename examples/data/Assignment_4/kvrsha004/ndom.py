#Q2 Assignment 4
#KVRSHA004
#Shaheel Kooverjee

def ndom_to_decimal(a):
   x = a%100
   y = x%10
   decimal = ((a//100)*36) + ((x//10)*6) + y
   return decimal

def decimal_to_ndom(a):
   x = a%36
   y = x%6
   ndom = ((a//36)*100) + ((x//6)*10) + y
   return ndom

def ndom_add(a, b):
   x = ndom_to_decimal(a)
   y = ndom_to_decimal(b)
   return decimal_to_ndom(x+y)

def ndom_multiply(a, b):
   x = ndom_to_decimal(a)
   y = ndom_to_decimal(b)
   return decimal_to_ndom(x*y)
   