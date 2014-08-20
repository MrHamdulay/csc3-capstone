"""Dumisani Ngwenza
NGWDUM005
02/04/2014"""

def ndom_to_decimal(x):
 """Converts a decimal number to Ndom"""
 x = x
 x = str(x)
 length = len(x)
 answer = 0
 i = 0
 
 while i<=length:
  base = int(x[i])
  multiple = base*(6**(length-1))
  length -=1
  i += 1
  answer += multiple
 return answer 
 
def decimal_to_ndom(x):
 """Converts a base 6 number (Ndom) to a decimal"""
 x = x
 length = len(str(x))
 answer = " "
 i = 0
 while length>=2:
  base = x//6
  remainder = x%6
  remainder = str(remainder)
  answer += remainder
  if base<6:
   base = str(base)
   answer += base
  length -= 1
   
  answer = answer[::-1]
  return answer


def ndom_add(a, b):
 """Adds 2 Ndom numbers (2 base 6 numbers)"""
 a, b = a, b
 units = 0
 answer = ' '
 a_string = str(a)
 b_string = str(b)
 length_a = int(len(a_string))
 length_b = int(len(b_string)) 
 
 if length_a > length_b:
    b_string = '0'*(length_a-length_b) + b_string
 elif length_b> length_a:
    a_string = '0'*(length_b-length_a) + a_string
    
 base = 0
 while 1<=length_a:
  a_unit = int(a_string[length_a-1])
  b_unit = int(b_string[length_b-1])
  base += a_unit + b_unit
  if base%6==0:
   if (int(a_string[0]) + int(b_string[0]))%6==0:
       answer += '0' + str(base//6)
   else:
    answer += '0'
   base += base//6
  elif base<6:
   answer += str(base)
   base = 0
  elif base>6:
   answer += str(base%6)
   base += base//6
  length_a -=1
  length_b -=1
     
 print(answer[::-1])
 
 
if __name__=="__main__":
 ndom_to_decimal(12)
 decimal_to_ndom(20)
 ndom_add(123, 41)
 ndom_to_decimal(20)
 decimal_to_ndom(12)