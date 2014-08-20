import ndom

green = input ("Choose test:\n")

colour = green[:1]

print ("calling function")

if colour == 'n' or colour == 'd':
   number = int(green[2:])
   if colour == 'n':
      ans = ndom.ndom_to_decimal (number)
   else:
      ans = ndom.decimal_to_ndom(number)
elif colour == 'a' or colour == 'm':
   number1, number2 = map (int, green[2:].split(" "))
   if colour == 'a':
      ans = ndom.ndom_add (number1, number2)
   else:
      ans = ndom.ndom_multiply (number1, number2)
      
print ("called function")

print (ans)
