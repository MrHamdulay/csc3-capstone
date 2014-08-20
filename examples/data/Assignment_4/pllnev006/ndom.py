# Module containing functions for Ndom calculations
# Nevarr Pillay - PLLNEV006
# 29 March 2014

def ndom_to_decimal(num):
     newnum = 0
     count = 0
     while num:
          newnum += num%10*(6**count)
          num = num//10
          count+=1
     return newnum     

def decimal_to_ndom(num):
     newnum = 0
     count = 0
     while num:
          newnum += num%6*(10**count)
          num = num//6
          count+=1
     return newnum


def ndom_add(a,b):
     sum = ndom_to_decimal(a)+ndom_to_decimal(b)
     return decimal_to_ndom(sum)     
    
def ndom_multiply(a,b):    
     product = ndom_to_decimal(a)*ndom_to_decimal(b)
     return decimal_to_ndom(product)   





        
        
    