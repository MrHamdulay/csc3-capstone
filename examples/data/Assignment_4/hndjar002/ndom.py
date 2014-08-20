# Pragram to show ndom* language
# Jaren Hendricks
# 03 April 2014

def ndom_to_decimal (a):
     floor = a//10
     rem = a%10
     equ = (floor * 6) + rem
     return equ 
    
    
def decimal_to_ndom (a):
     floor = a//6
     rem1 = a%6
     rem2= floor%6
     Equ= ((rem2*10)+rem1)
     return Equ
    
def ndom_add (a, b):
     Aans = ndom_to_decimal (a)
     Bans = ndom_to_decimal (b)
     FinalAns = Aans + Bans
     dec = ndom_to_decimal (FinalAns)
     return dec
     
    
def ndom_multiply (a, b):
     Aans = ndom_to_decimal (a)
     Bans = ndom_to_decimal (b)
     FinalAns = Aans * Bans
     dec = decimal_to_ndom (FinalAns)
     return dec
    

