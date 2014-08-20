# Message encryption
# Michael Sanne
# 2014/05/05

#Takes message and encrypts each individual character as long as it is in lower case
def encrypter (String, position):
    newString = ""
    if (position == len(String)):
        return newString
    else:
        #Checks for character in lower case and converts it
        if (97 <= ord(String[position]) < 122):
            newString += chr(ord(String[position])+1)
        #if z make it a
        elif (ord(String[position]) == 122):
                newString += chr(97)
        else:
            newString += String[position]
        return newString + encrypter (String, position+1)

#Asks user for input message
String = input ("Enter a message:\n")
String.lower()
print ("Encrypted message:")
print(encrypter (String, 0))