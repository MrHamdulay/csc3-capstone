#Liam Brodie
#02/04/2014

def ndom_to_decimal(a): #converts from base 6 to base 10
     
     loopcount = 0;
     while True:
          if a == decimal_to_ndom(loopcount):
               return loopcount
          else:
               loopcount+=1
               
          

def decimal_to_ndom(a):  #converts from base 10 to base 6
    
     result = ""
     
     if (a == 0): 
          result = "0"
     else: 
          a
          while a > 0: 
               remainder = a % 6 
               result = str(remainder) + result 
               a = a // 6 
     
     return int(result)



def ndom_add(a,b):
     a = ndom_to_decimal(a)
     b = ndom_to_decimal(b)
     
     DecimalAnswer = a +b
     
     return decimal_to_ndom(DecimalAnswer)



def ndom_multiply(a,b):
     a = ndom_to_decimal(a)
     b = ndom_to_decimal(b)
          
     DecimalAnswer =  a*b    
     
     return decimal_to_ndom(DecimalAnswer)