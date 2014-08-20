# test program for Ndom calculations

import ndom

c = input ("Choose test:\n")
a = c[:1]
print ("calling function")
if a == 'n' or a == 'd':
   num = int(c[2:])
   if a == 'n':
      ans = ndom.ndom_to_decimal (num)
   else:
      ans= ndom.decimal_to_ndom(num)
elif a == 'a' or a == 'm':
   num1, num2 = map (int, c[2:].split(" "))
   if a == 'a':
      ans = ndom.ndom_add (num1, num2)
   else:
      ans = ndom.ndom_multiply (num1, num2)
print ("called function")
print (ans)
