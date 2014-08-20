'''Assignment8,q3 encrpytion recursion
Kieran Reilly, RLLKIE001
06/05/14'''



def encryptor(userString, outString):
    '''encrypts a message, by shifting the alphabet by 1, and wrapping'''
    #basecase - checks the string length is greater or equal to one
    if len(userString) >= 1:
        #recursive case - checks if the current character is lower or upper case
        if userString[0].islower():
            asciiCode = ord(userString[0])
            #recursive step - does encryption if the character = a
            if(asciiCode == 122):
                asciiCode = asciiCode - 25
                outString = outString + str(chr(asciiCode))
                outString = encryptor(userString[1:], outString)
            #recursive step - does encryption if the character = z
            else:
                asciiCode = asciiCode + 1
                outString = outString + str(chr(asciiCode))
                outString = encryptor(userString[1:], outString)
        else:
            outString = outString + userString[0]
            outString = encryptor(userString[1:], outString)
    return outString
    
def main():
    outString = ""
    userString = input("Enter a message:\n")
    message = encryptor(userString, outString)
    print("Encrypted message:\n" + message)
    



main()