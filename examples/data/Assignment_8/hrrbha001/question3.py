def encrypt ( str ):
   if str == "":
      return ""
   elif (ord (str[0]) > 96 and ord (str[0]) < 123):
      return chr ((ord (str[0]) - 70) % 26 + 97) + encrypt (str[1:])
   else:
      return str[0] + encrypt (str[1:])

str = input ("Enter a message:\n")
print ("Encrypted message:\n"+encrypt (str))

