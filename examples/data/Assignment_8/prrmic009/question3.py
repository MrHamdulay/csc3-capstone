"""Program to encrypt message by changing each letter to the following letter in the alphabet
Mick Perring
08 May 2014"""
        
message = str(input("Enter a message:\n"))

def encrypt(message, new):   # encrypt function to encrypt input message
   if len(message) >= 1:
        
      if (ord(message[0])) < 97 or (ord(message[0])) > 122:  # checks for uppercase letters in string
         new += (message[0])                                  # to leave them as they are
         return encrypt(message[1:], new)                  
          
      if message[0] == ("z"):  # converts last letter of alphabet(z) to first letter of alphabet(a)
         new += ("a")
         return encrypt(message[1:], new)
       
      else:                   # converts all remaining letters to the next letter in the alphabet
         new += chr(ord(message[0])+1)
         return encrypt(message[1:], new) 
       
   if len(message) == 0:  # prints out new encrypted message
      print("Encrypted message:\n" + new)

encrypt(message, "")               