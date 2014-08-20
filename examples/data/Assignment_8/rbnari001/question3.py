#Ariel Rubin
#RBNARI001
#program to encrypt a string recursively
#9 may 2014

#function used to encrypt a string
def encrypt (sentence):
    #if there is no message to encrypt then returns a blank string
    if len(sentence) == 0:
        return ''
    #uses unicode to find the vale of each letter in the string
    if (ord(sentence[0])>= 97) and (ord (sentence[0])<= 122):
        if sentence[0] == 'z':
            return 'a' + encrypt(sentence[1:])
        else:
            return chr(ord(sentence[0])+1) + encrypt(sentence[1:])
    else:
        return sentence[0] + encrypt(sentence[1:])
    
#ask useer to enter a message
message = input ("Enter a message:\n")
#displays encrypted message
print ("Encrypted message:")
print(encrypt(message))
