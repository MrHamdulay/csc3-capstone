# test program for Ndom calculations

import ndom

choice = input ("Choose test:\n")
action = choice[:1]
print ("calling function")
if action == 'n' or action == 'd':
   num = int(choice[2:])
   if action == 'n':
      ndom.ndom_to_decimal (num)
   else:
      ndom.decimal_to_ndom(num)
elif action == 'a' or action == 'm':
   num1, num2 = map (int, choice[2:].split(" "))
   if action == 'a':
      ndom.ndom_add (num1, num2)
   else:
      ndom.ndom_multiply (num1, num2)
print ("called function")

