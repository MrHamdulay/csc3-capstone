# Thembekani Gwegwana
# A program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a).
# April 2014

message=input('Enter a message:\n')
def encrypt(string):
  if string == '' :
    return ''
  #Checks if the string contains z and replaces it with a
  elif string[0] == 'z' :
    return 'a' + encrypt(string[1:])
  #Checks if the string is lowercase
  elif string[0].islower():
    new_string= ord(string[0]) +1
    return chr(new_string) +encrypt(string[1:])
  #If the string begins with a capital letter, return the letter and encrypts the rest
  else :
    return string[0] + encrypt(string[1:])
print('Encrypted message:\n', encrypt(message), sep='')
    
  
  