# test program for Ndom calculations

import ndom

option = input ("Choose test:\n")
choice = choice[:1]
print ("calling function")
if choice == 'n' or choice == 'd':
   num = int(option[2:])
   if choice == 'n':
      answer = ndom.ndom_to_decimal (num)
   else:
      answer = ndom.decimal_to_ndom(num)
elif action == 'a' or action == 'm':
   num1, num2 = map (int, choice[2:].split(" "))
   if choice == 'a':
      answer = ndom.ndom_add (num1, num2)
   else:
      answer = ndom.ndom_multiply (num1, num2)
print ("called function")
print (answer)
