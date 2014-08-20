#R.Eyre
#01/04/2014

def ndom_to_decimal(a):
     """converts base 6 to base 10"""
     
     count = 0;
     while True:
          if a== decimal_to_ndom(count):
               return count
          else:
               count+=1
          

def decimal_to_ndom(a):
     """converts base 10 to base 6"""
     num = a
     result = ""
     
     if (num == 0): 
          result = "0"
     else: 
          quotient = num 
          #result = "0" 
          while quotient > 0: 
               remainder = quotient % 6 
               result = str(remainder) + result 
               quotient = quotient // 6 
     
     return int(result)

def ndom_add(a,b):
     n1 = ndom_to_decimal(a)
     n2 = ndom_to_decimal(b)
     
     decAns = n1 + n2
     
     return decimal_to_ndom(decAns)

def ndom_multiply(a,b):
     n1 = ndom_to_decimal(a)
     n2 = ndom_to_decimal(b)
          
     decAns = n1*n2     
     
     return decimal_to_ndom(decAns)