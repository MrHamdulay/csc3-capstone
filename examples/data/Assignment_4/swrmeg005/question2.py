import ndom

choice = input ("Choose test:\n")
action = choice[:1]
print ("calling function")
if action == 'n' or action == 'd':
   num = int(choice[2:])
   if action == 'n':
      answer = ndom.ndom_to_decimal (num)
   else:
      answer = ndom.decimal_to_ndom(num)
elif action == 'a' or action == 'm':
   num1, num2 = map (int, choice[2:].split(" "))
   if action == 'a':
      answer = ndom.ndom_add (num1, num2)
   else:
      answer = ndom.ndom_multiply (num1, num2)
print ("called function")
print (answer)
