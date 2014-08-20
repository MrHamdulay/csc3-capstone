import ndom
def ndom_to_decimal (a): 
   string = str(a)
   a= 1 
   while a < len(string):
      if len(string)== 4:
         converter =(int(string[0])*216) + (int(string[1])*36)+(int(string[2])*6)+(int(string[3])*1)
         a+=1
      elif len(string) == 3:
         converter =((int(string[0])*36)+(int(string[1])*6)+(int(string[2])*1))
         a+=1
      elif len(string) == 2:
         converter =((int(string[0])*6)+(int(string[1])*1))
         a+=1 
      elif len(string) == 1:
         converter =((int(string[0])*1))
         a+=1      
   return converter
def decimal_to_ndom(a):
   calculator = a 
   string = ""
   while calculator >0 : 
      lastdigit= calculator%6
      calculator= calculator//6
      string += str(lastdigit)
   return int(string[::-1])


def ndom_add (a, b):
   number1 = ndom.ndom_to_decimal(a)
   number2 = ndom.ndom_to_decimal(b)
   decimal = number1 + number2
   value = ndom.decimal_to_ndom(decimal)
   return value

def ndom_multiply (a, b):
   number1 = ndom.ndom_to_decimal(a)
   number2 = ndom.ndom_to_decimal(b)
   decimal = number1 * number2
   value = ndom.decimal_to_ndom(decimal)
   return value   
  