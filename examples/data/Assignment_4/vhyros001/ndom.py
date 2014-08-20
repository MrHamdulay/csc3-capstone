"""Convert base 6 to decimal and back, add and multiply base 6
Ross van der Heyde VHYROS001
31 March 2014"""


def decimal_to_ndom (a):
   num = ""
   num = str(a//36)   
   
   #print ("first:", a//36)
   
   #second digit
   b = a - (a//36)*36
   #print ("b: ", b)
   num += str(b//6)
   #print("num: ", num)
      
   #third digit
   num += str(a%6)
   
   #trim
   if num [0]=="0":
      if num[1]=="0":
         num = num [2]
      else:
         num = num[1:3]   
   
   return num

# receive ndom, convert to decimal, return
def ndom_to_decimal (a):
   a = str(a)
   decimal =0      
   l = len(a)      
      
   for i in range (l):      
      decimal+= int(a[l-i-1])*(6**i)
      
   return decimal
      
# add 2 ndom numbers
def ndom_add (a, b):
   sum = ndom_to_decimal(a) + ndom_to_decimal(b)
   return decimal_to_ndom(sum)
    
# multiply ndom numbers
def ndom_multiply (a,b):
   prod = int(ndom_to_decimal(a)) * int(ndom_to_decimal(b))
   return decimal_to_ndom(prod)

#In the Ndom* language, numbers use only the digits 0-5, such that instead of "tens" and "hundreds", the 
#second and third digits represents multiples of 6 and 36 respectively. Write a Python module with the 
#following functions for simple Ndom arithmetic, assuming that all values have at most 3 digits.
#(Reference: http://en.wikipedia.org/wiki/Senary)

#ndom_to_decimal (a), that converts a Ndom number to decimal
#decimal_to_ndom (a), that converts a decimal number to Ndom
#ndom_add (a, b), that adds 2 Ndom numbers
#ndom_multiply (a, b), that multiples 2 Ndom numbers




 #second digit
   #if a %6 != 0 and a % 6 !=6:
      #print ("str(a//6):",str(a//6))
      #num += str(a//6)
   #else:
      #if a % 6 ==0:
         #num+=str(a//6)
      
      #num +="0"
   
   # third digit
   #num+= str(a%6)
   #print("num=",num) 
   
   #trim
   #if num [0]=="0":
      #if num[1]=="0":
         #num = num [2]
      #else:
         #num = num[1:3]