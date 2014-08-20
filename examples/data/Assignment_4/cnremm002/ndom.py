def decimal_to_ndom(num):
     baseN = 0
     n=1
     
     while num//n != 0:
          n+=1
          
     for i in range(n-1,-1,-1):
          tempDigit = (num//6**i) * (10**i)     
          baseN += tempDigit
          num = num%6**i
         
     return baseN

def ndom_to_decimal(num):     
     n = 0
     base10 = 0
     
     for i in range(-1,-len(str(num))-1,-1):
          base10 += eval(str(num)[i]) * 6**n
          n += 1
          
     return base10

def ndom_add(a,b):
     sumDecimal = ndom_to_decimal(a)+ndom_to_decimal(b)
     sumBase = decimal_to_ndom(sumDecimal)
     return sumBase

def ndom_multiply(a,b):
     productDecimal = ndom_to_decimal(a)*ndom_to_decimal(b)
     productBase = decimal_to_ndom(productDecimal)
     return productBase