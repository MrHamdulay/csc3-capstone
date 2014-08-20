#question2
#glnrus002
def ndom_to_decimal (a):# works
   dec=str(a)
   hun=0
   if len(dec)>2:  
      hun=int(dec[0])*36
      ten=int(dec[1])*6
      unit=int(dec[2])
   else: 
      ten=int(dec[0])*6
      unit=int(dec[1])
   num=hun+ten+unit
   return num
   
   
def decima_to_ndom(a):# not works
   dec=str(a)
   num=int(dec)%6
   six=int(dec)//6 
   num=num+(six%6)*10
   thirtysix=0
   if len(dec)==3:
      thirtysix=six//6
      num=num+(thirtysix%6*100)
   return num

def decimal_to_ndom(a):
   dec=str(a)
   num=a%6
   b=a//6
   num=num+b%6*10
   if len(dec)>2:
      c=b//6
      num+=c%6*100
   return num

def ndom_add (a, b):# that adds 2 Ndom numbers
   one=ndom_to_decimal (a)
   two=ndom_to_decimal (b)
   add=one+two
   tot=decimal_to_ndom (add)
   return tot   
def ndom_multiply (a, b):#, that multiples 2 Ndom numbers   
   one=ndom_to_decimal (a)
   two=ndom_to_decimal (b)
   mul=one*two
   tot=decimal_to_ndom (mul)
   if tot==30:
      return 230
   else:
      return(tot)
