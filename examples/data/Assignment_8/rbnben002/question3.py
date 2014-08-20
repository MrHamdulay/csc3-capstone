def encrypt (sentence):
    if len(sentence) == 0:
        return ''
    if (ord(sentence[0])>= 97) and (ord (sentence[0])<= 122):
        if sentence[0] == 'z':
            return 'a' + encrypt(sentence[1:])
        else:
            return chr(ord(sentence[0])+1) + encrypt(sentence[1:])
    else:
        return sentence[0] + encrypt(sentence[1:])
   
user = input ("Enter a message:\n")
print ("Encrypted message:")
print(encrypt(user))