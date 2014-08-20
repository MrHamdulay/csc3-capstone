#Jade Petersen
#Assignment 4
#ndom
#4 april 2014

def decimal_to_ndom(num):
     baseN = 0
     p=1
     
     while num//p != 0:
          p+=1
          
     for i in range(p-1,-1,-1):
          tempDigit = (num//6**i) * (10**i)     
          baseN += tempDigit
          num = num%6**i
         
     return baseN

def ndom_to_decimal(num):     
     p = 0
     base10 = 0
     
     for i in range(-1,-len(str(num))-1,-1):
          base10 += eval(str(num)[i]) * 6**p
          p += 1
          
     return base10

def ndom_add(a,b):
     sumDecimal = ndom_to_decimal(a)+ndom_to_decimal(b)
     sumBase = decimal_to_ndom(sumDecimal)
     return sumBase

def ndom_multiply(a,b):
     productDecimal = ndom_to_decimal(a)*ndom_to_decimal(b)
     productBase = decimal_to_ndom(productDecimal)
     return productBase