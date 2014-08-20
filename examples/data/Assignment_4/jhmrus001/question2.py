import ndom

choice = input ("Choose test:\n")
action = choice[:1]
print ("calling function")
if action == 'n' or action == 'd':
   number = int(choice[2:])
   if action == 'n':
      solution = ndom.ndom_to_decimal (number)
   else:
      solution = ndom.decimal_to_ndom(number)
elif action == 'a' or action == 'm':
   number1, number2 = map (int, choice[2:].split(" "))
   if action == 'a':
      solution = ndom.ndom_add (number1, number2)
   else:
      solution = ndom.ndom_multiply (number1, number2)
print ("called function")
print (solution)
