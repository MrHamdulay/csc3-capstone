# Encrypts a message using recursion
# Conor O'Sullivan
# 04/05/2014


# Get input
sent = input("Enter a message:\n")

#Incursive function
def encrypt(sent):
       if sent == "":
              return ""
       elif sent[0] == 'z':
              return 'a' + encrypt(sent[1:])
       elif   97 > ord(sent[0]):
              return sent[0] + encrypt(sent[1:])
       elif sent[0] == ' ':
              return ' ' + encrypt(sent[1:])
       else:
              new_ord = ord(sent[0]) +1
              return chr(new_ord) + encrypt(sent[1:])
       
       
       
print("Encrypted message:\n" +  encrypt(sent))
       