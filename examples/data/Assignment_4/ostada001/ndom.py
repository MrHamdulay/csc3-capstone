"""
Adam Oosthuizen
Module for Q2, Assignment 4
31 March 2014
"""
digits = 0

def noDigits(a):
 return len(str(a))

def ndom_to_decimal (a):
 b = 0
 s = str(a)
 if len(s) == 3:
  b = (eval(s[0]))*36 + (eval(s[1]))*6 +(eval(s[2]))
   
 elif len(s) == 2:
   b =  (eval(s[0]))*6 +(eval(s[1]))
     
 elif noDigits(a) == 1:
   b = a 
 return b

def decimal_to_ndom (a):
 #converts a decimal number to Ndom
  b = (a-(a%36))//36*100
  c = ((a%36) - ((a%36)%6))//6*10
  d = ((a%36)%6)
  return b + c + d

def ndom_add (a, b):
 #adds 2 Ndom numbers
 return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))

def ndom_multiply (a, b):
 #multiples 2 Ndom numbers
 return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))