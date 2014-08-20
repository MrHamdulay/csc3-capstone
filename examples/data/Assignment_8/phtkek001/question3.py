"""Kekolo Phetla
phtkek001"""

string=input("Enter a message:\n")
def encrypt(string):
  if len(string)<1:
    return " "
  elif string[0].islower()==False:
    return string[0]+encrypt(string[1:])
  elif string[0]=="z":
    return "a" + encrypt(string[1:])
  else:
    new_string=(ord(string[0])+1)
    return chr(new_string) + encrypt(string[1:])
  
print("Encrypted message:")
print(encrypt(string))



  
 