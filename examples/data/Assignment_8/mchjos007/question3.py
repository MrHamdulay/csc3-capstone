def encryptThisMother(theStringToBeEncrypted):
    if len(theStringToBeEncrypted) == 0:
        return ''
    if (ord(theStringToBeEncrypted[0]) >= 97 and ord(theStringToBeEncrypted[0])<=122):
        if theStringToBeEncrypted[0] == 'z':
            return 'a' + encryptThisMother(theStringToBeEncrypted[1:])
        else:
            return chr(ord(theStringToBeEncrypted[0])+1) + encryptThisMother(theStringToBeEncrypted[1:])
    else:
        return theStringToBeEncrypted[0] +encryptThisMother(theStringToBeEncrypted[1:])
    

theMessage = input("Enter a message:\n")
print("Encrypted message:")
print(encryptThisMother(theMessage))