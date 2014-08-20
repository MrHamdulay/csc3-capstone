#Joy Arendse-Gorvalla
def encrypt (s): #defining a function
    if len(s) == 0: #if there is no message then it returns a blank string
        return ''
    if (ord(s[0])>= 97) and (ord (s[0])<= 122): #use unicode to find the vale of each letter in the string
        if s[0] == 'z':
            return 'a' + encrypt(s[1:])
        else:
            return chr(ord(s[0])+1) + encrypt(s[1:])
    else:
        return s[0] + encrypt(s[1:])
    
message = input ("Enter a message:\n") #asks user to enter a message
print ("Encrypted message:")
print(encrypt(message)) #prints out the encrypted message