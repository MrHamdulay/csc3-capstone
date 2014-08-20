#Thea Sitek, STKTHE002
#09.05.2014
#Decrypt text

def decrypt(crypt):
    
    length = len(crypt)
    
    if crypt == "" or crypt == " ":
        return ""
    else:
        if not crypt[0].isalpha():
            return crypt[0] + decrypt(crypt[1:])
        elif crypt[0]== crypt[0].lower():
            if (ord(crypt[0])) <= 121 and (ord(crypt[0])) >= 97:
                value = 1 + ord(crypt[0])
                return chr(value) + decrypt(crypt[1:])
            elif (ord(crypt[0])) == 122:
                return 'a' + decrypt(crypt[1:])
        else: #if crypt[0] == crypt[0].upper():
            return crypt[0] + decrypt(crypt[1:])


message = input('Enter a message: \n')
if decrypt(message):
    print('Encrypted message:')
    print(decrypt(message))
